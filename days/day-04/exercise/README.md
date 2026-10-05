# Day 4 Exercise: Test the Reading-List API + Configuration from the Environment

| | |
|---|---|
| **What you will practice** | Writing `APITestCase` tests (arrange → act → assert) · testing success **and** failure cases · checking the database inside a test · reading a failing test · moving settings to environment variables · documenting them in `.env.example` |
| **Where to start** | This folder: `days/day-04/exercise/`. Files: `catalog/tests.py` (Task 1) → `config/settings.py` + `.env.example` (Task 2) → `catalog/views.py` (Task 3, a temporary experiment) |
| **Result to produce** | `python manage.py test` → **Ran 9 tests ... OK** with **no skipped tests**, settings that change when environment variables change, and a placeholder-only `.env.example` |
| **Time** | ~60 minutes |
| **Hints** | [`../hints.md`](../hints.md) · worked example: [`../example/`](../example/) |

---

## Before you start

Run these in a terminal **opened in this folder** (`days/day-04/exercise`):

```bash
..\..\..\.venv\Scripts\Activate.ps1          # Windows PowerShell
source ../../../.venv/bin/activate            # macOS

python manage.py test                         # -> Ran 9 tests ... OK (skipped=8)  <- your starting point
```

> **Database state:** the tests do **not** use `db.sqlite3` or the sample data. Each test gets a fresh, empty
> temporary database and `setUp()` creates the data listed below.
>
> The API itself is the finished Day 3 reading-list API (token auth, ownership, validation), so there is nothing to fix
> in it. If you also want to click through it manually, the usual commands work and load the same demo users as Day 3:
> `python manage.py migrate`, then `python manage.py loaddata sample_data` (14 objects; `alice` / `alice-pass-2026`,
> `bob` / `bob-pass-2026`), then `python manage.py runserver`.

---

## Task 1: Write the tests

**File:** `catalog/tests.py`. One test is complete (`test_no_token_returns_401`). Replace each
`self.skipTest(...)` line in the 8 `TODO [Day 4 · Task 1-n]` tests with real code.

**Test data created by `setUp()`** (new for every test; ids are not predictable, so always use the attributes):

| Attribute | What it is |
|---|---|
| `self.alice`, `self.bob` | users (passwords `alice-test-pass`, `bob-test-pass`) |
| `self.alice_token`, `self.bob_token` | their DRF tokens |
| `self.book_1`, `self.book_2` | books "Clean Code" and "Refactoring" |
| `self.alice_item` | alice's reading-list item: `book_1`, status `READING` |
| `self.bob_item` | bob's reading-list item: `book_2`, status `WANT_TO_READ` |
| `self.list_url`, `self.alice_item_url` | `/api/reading-list/` and `/api/reading-list/<alice_item.id>/` |
| `self.use_token(token)` | helper: sends `Authorization: Token <key>` on the next requests |

**What each test must prove**

| # | Test | Act (request) | Assert (response) | Assert (database) |
|---|---|---|---|---|
| 1 | `test_token_login_returns_token` | POST `/api/auth/token/` with alice's credentials | `200`, `token` == `self.alice_token.key` | none |
| 2 | `test_list_shows_only_my_items` | alice: GET list | `200`, ids == `[alice_item.id]` | none |
| 3 | `test_create_sets_user_from_token` | bob: POST `{"book": book_1.id, "user": alice.id}` | `201`, `user` == `"bob"` | new row's `user` is bob |
| 4 | `test_other_users_item_returns_404` | bob: GET alice's item | `404` | none |
| 5 | `test_other_user_cannot_delete_my_item` | bob: DELETE alice's item | `404` | alice's item still exists |
| 6 | `test_past_target_date_returns_400` | alice: POST book_2 with yesterday's date | `400`, `target_date` in errors | none |
| 7 | `test_duplicate_book_returns_400` | alice: POST book_1 again | `400`, `book` in errors | alice still has 1 item |
| 8 | `test_patch_updates_only_status` | alice: PATCH `{"status": "FINISHED"}` | `200` | status `FINISHED`, book unchanged |

**Acceptance criteria**
- [ ] `python manage.py test` → `Ran 9 tests ... OK` and **no** `skipped=` in the summary.
- [ ] Every test checks the status code; tests 3, 5, 7, 8 also check the database.

---

## Task 2: Settings from environment variables

**Files:** `config/settings.py` (`TODO Task 2a`) and `.env.example` (`TODO Task 2b`).

| Variable | Default when not set | Python value |
|---|---|---|
| `SECRET_KEY` | `exercise-only-key` | string |
| `DEBUG` | `True` | **bool**: `True` only when the text is `true`/`True` |
| `ALLOWED_HOSTS` | `127.0.0.1,localhost` | **list**, e.g. `["127.0.0.1", "localhost"]` |

**Check your work:** `show_settings.py` (given) prints what Django loaded.

```bash
python show_settings.py
#   DEBUG         : True  (bool)
#   ALLOWED_HOSTS : ['127.0.0.1', 'localhost']
```

Now set variables **in the same terminal** and run it again:

```powershell
# Windows PowerShell
$env:DEBUG = "False"; $env:SECRET_KEY = "any-long-test-value"; $env:ALLOWED_HOSTS = "example.com, api.example.com"
python show_settings.py
Remove-Item Env:DEBUG, Env:SECRET_KEY, Env:ALLOWED_HOSTS      # clean up afterwards
```

```bash
# macOS
DEBUG=False SECRET_KEY=any-long-test-value ALLOWED_HOSTS="example.com, api.example.com" python show_settings.py
```

**Expected output with the variables set**

```text
SECRET_KEY    : ******** (from environment, 19 characters)
DEBUG         : False  (bool)
ALLOWED_HOSTS : ['example.com', 'api.example.com']
```

Then complete `.env.example`: one line per variable with a comment and a **placeholder** value.

**Acceptance criteria**
- [ ] With no variables set, the defaults print. With variables set, the new values print with the right types.
- [ ] `.env.example` lists all three variables and contains **no real secret**.
- [ ] `python manage.py test` still passes.

---

## Task 3: Watch a test catch a security bug (experiment, then undo)

**File:** `catalog/views.py`. This task shows **why** tests matter.

1. In `ReadingListItemViewSet.get_queryset`, temporarily change the line to
   `return ReadingListItem.objects.all()` (everyone's items, the Day 3 bug).
2. Run `python manage.py test`.
3. Write down **which tests fail** and the **first assertion message** of one failure (`AssertionError: ...`).
4. **Restore** the original line and confirm all tests pass again.

**Expected result:** tests 2, 4 and 5 fail, because the API leaks other users' data. Fix the application, never the
test's expectation.

**Acceptance criteria**
- [ ] You can name the failing tests and explain each failure in one sentence.
- [ ] `views.py` is restored and the suite is green.

---

## Done? Check yourself

- [ ] I can explain why tests create their own data instead of using my `db.sqlite3`.
- [ ] I can explain why `SECRET_KEY` must not be written in `settings.py` for production.
- [ ] Now apply the same ideas to the project: [`../project-milestone.md`](../project-milestone.md)
