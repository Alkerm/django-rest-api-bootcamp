# Day 4 Exercise: Test the Reading-List API

| | |
|---|---|
| **What you will practice** | Writing `APITestCase` tests (arrange → act → assert) · testing success **and** failure cases · checking the database inside a test · reading a failing test |
| **Where to start** | This folder: `days/day-04/exercise/`. Files: `catalog/tests.py` (Task 1) → `catalog/views.py` (Task 2, a temporary experiment) |
| **Result to produce** | **Core:** the 4 REQUIRED tests pass (`OK (skipped=4)`). **Stretch:** the 4 STRETCH tests and Task 2 |
| **Time** | ~45 minutes for the core; stretch only if you finish early (the project milestone comes first) |
| **Hints** | [`../hints.md`](../hints.md) · worked example: [`../example/`](../example/) |

---

## Before you start

Run these in a terminal **opened in this folder** (`days/day-04/exercise`):

```bash
..\..\..\.venv\Scripts\Activate.ps1          # Windows PowerShell
source ../../../.venv/bin/activate            # macOS

python manage.py test                         # -> Ran 9 tests ... OK (skipped=8)  <- your starting point
python manage.py test -v 2                    # lists every test and whether it is REQUIRED or STRETCH
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

**File:** `catalog/tests.py`. One test is complete (`test_no_token_returns_401`). Each other test is marked
**REQUIRED** (core: do these 4) or **STRETCH** (optional). Replace the test's `self.skipTest(...)` line with real code.

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

| # | Test | Level | Act (request) | Assert (response) | Assert (database) |
|---|---|---|---|---|---|
| 1 | `test_token_login_returns_token` | **REQUIRED** | POST `/api/auth/token/` with alice's credentials | `200`, `token` == `self.alice_token.key` | none |
| 2 | `test_list_shows_only_my_items` | **REQUIRED** | alice: GET list | `200`, ids == `[alice_item.id]` | none |
| 3 | `test_create_sets_user_from_token` | stretch | bob: POST `{"book": book_1.id, "user": alice.id}` | `201`, `user` == `"bob"` | new row's `user` is bob |
| 4 | `test_other_users_item_returns_404` | **REQUIRED** | bob: GET alice's item | `404` | none |
| 5 | `test_other_user_cannot_delete_my_item` | stretch | bob: DELETE alice's item | `404` | alice's item still exists |
| 6 | `test_past_target_date_returns_400` | **REQUIRED** | alice: POST book_2 with yesterday's date | `400`, `target_date` in errors | none |
| 7 | `test_duplicate_book_returns_400` | stretch | alice: POST book_1 again | `400`, `book` in errors | alice still has 1 item |
| 8 | `test_patch_updates_only_status` | stretch | alice: PATCH `{"status": "FINISHED"}` | `200` | status `FINISHED`, book unchanged |

**Acceptance criteria**
- [ ] **Core:** `python manage.py test` → `OK (skipped=4)`. The 4 skipped are the STRETCH tests.
- [ ] Every test you wrote checks the status code. Stretch tests 3, 5, 7, 8 also check the database.
- [ ] *Stretch:* `Ran 9 tests ... OK` with no `skipped=`.

---

## Task 2 (STRETCH, optional): Watch a test catch a security bug (experiment, then undo)

**File:** `catalog/views.py`. This task shows **why** tests matter.

1. In `ReadingListItemViewSet.get_queryset`, temporarily change the line to
   `return ReadingListItem.objects.all()` (everyone's items, the Day 3 bug).
2. Run `python manage.py test`.
3. Write down **which tests fail** and the **first assertion message** of one failure (`AssertionError: ...`).
4. **Restore** the original line and confirm all tests pass again.

**Expected result:** tests 2 and 4 fail (and 5, if you wrote it), because the API leaks other users' data. Fix the application, never the
test's expectation.

**Acceptance criteria**
- [ ] You can name the failing tests and explain each failure in one sentence.
- [ ] `views.py` is restored and the suite is green.

---

## Done? Check yourself

- [ ] I can explain why tests create their own data instead of using my `db.sqlite3`.
- [ ] Now apply the same ideas to the project: [`../project-milestone.md`](../project-milestone.md)
