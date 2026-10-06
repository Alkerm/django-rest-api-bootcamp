# Day 3 Exercise: Personal Reading List (Token Auth, Ownership, Validation)

| | |
|---|---|
| **What you will practice** | Enabling DRF token authentication · protecting endpoints · filtering a queryset by `request.user` · setting the owner on the server · field validation with clear error messages |
| **Where to start** | This folder: `days/day-03/exercise/`. Files: `config/settings.py` + `config/urls.py` (Task 1) → `catalog/views.py` (Task 2) → `catalog/serializers.py` (Task 3) |
| **Result to produce** | **Core (Tasks 1-2):** Alice and Bob each get a token and each sees and changes **only their own** reading list; `python manage.py test -k task1 -k task2` → **Ran 6 tests ... OK**. **Stretch (Task 3):** validation errors; all 11 tests pass |
| **Time** | ~35 minutes for the core; Task 3 only if you finish early (the project repeats validation) |
| **Hints** | [`../hints.md`](../hints.md) · worked example: [`../example/`](../example/) |

---

## Before you start

Run these in a terminal **opened in this folder** (`days/day-03/exercise`):

```bash
..\..\..\.venv\Scripts\Activate.ps1          # Windows PowerShell
source ../../../.venv/bin/activate            # macOS

python manage.py migrate                      # creates this exercise's db.sqlite3
python manage.py loaddata sample_data         # -> Installed 14 object(s) from 1 fixture(s)
python manage.py runserver
```

> **Your progress meter:** `python manage.py test -k task1` (then `-k task2`) in a 2nd terminal. The tests fail at
> the start, which is expected; each failure message names the task that fixes it.

> **Database state: pre-filled with sample data.** 2 users, 3 authors, 6 books, 3 reading-list items (tables in
> each task below). Every endpoint already **requires authentication**, so before Task 1 any request returns
> `403 Forbidden` because there is no way to log in yet.

**Demo accounts** (exercise-only test data, stored hashed in the fixture; never reuse these passwords anywhere):

| id | username | password |
|---|---|---|
| 1 | `alice` | `alice-pass-2026` |
| 2 | `bob` | `bob-pass-2026` |

Use **Postman** (recommended) or the browsable API. In Postman create an environment with `base_url` =
`http://127.0.0.1:8000` and an empty `token` variable (see [`setup/postman.md`](../../../setup/postman.md)).

---

## Task 1: Token authentication

**Files:** `config/settings.py` (`TODO Task 1a`, `TODO Task 1b`) and `config/urls.py` (`TODO Task 1c`, parts 1 + 2).

1. Add `rest_framework.authtoken` to `INSTALLED_APPS`, then run `python manage.py migrate`.
   **Database change:** a new table `authtoken_token` (`key` 40 chars, `user_id` one-to-one → `auth_user`, `created`).
   It is empty: a token row is created the first time a user logs in.
2. Add `DEFAULT_AUTHENTICATION_CLASSES` (Token first, then Session).
3. Add the login endpoint `api/auth/token/`.

**Expected input → output**

| Request | Expected response | Database change |
|---|---|---|
| `POST /api/auth/token/` `{"username": "alice", "password": "alice-pass-2026"}` | `200` `{"token": "9944b09199c62bcf..."}` (40 chars) | 1 row in `authtoken_token` for alice (same token on every later login) |
| `POST /api/auth/token/` `{"username": "alice", "password": "wrong"}` | `400` `{"non_field_errors": ["Unable to log in with provided credentials."]}` | none |
| `GET /api/reading-list/` with **no** `Authorization` header | `401` `{"detail": "Authentication credentials were not provided."}` | none |
| `GET /api/books/` with header `Authorization: Token <alice's token>` | `200` + 6 books | none |

**Acceptance criteria**
- [ ] `python manage.py test -k task1` → the 3 Task 1 tests pass.

---

## Task 2: Ownership: my list only

**File:** `catalog/views.py`. Find `TODO Task 2a` (`get_queryset`) and `TODO Task 2b` (`perform_create`).

**Table `catalog_readinglistitem`** (pre-loaded)

| id | user_id (owner) | book_id → title | status | target_date | notes |
|---|---|---|---|---|---|
| 1 | 1 → **alice** | 1 → Clean Code | `READING` | 2026-12-31 | Chapter 3 next |
| 2 | 1 → **alice** | 4 → Refactoring | `WANT_TO_READ` | null | |
| 3 | 2 → **bob** | 3 → Clean Architecture | `FINISHED` | null | Great overview |

Fields: `user` FK → `auth_user` (**read-only in the API, set by the server**) · `book` FK → `catalog_book` (send the
book id) · `status` one of `WANT_TO_READ` (default) / `READING` / `FINISHED` · `target_date` date or null · `notes` text
(optional) · `created_at` automatic. Rule: one user cannot have the same book twice.

**Expected input → output**

| Request (token of…) | Before Task 2 (bug) | Expected after Task 2 | Database change |
|---|---|---|---|
| alice: `GET /api/reading-list/` | items 1, 2, **3** (bob's item leaks!) | `200`, items **1, 2** only | none |
| bob: `GET /api/reading-list/` | items 1, 2, 3 | `200`, item **3** only | none |
| bob: `GET /api/reading-list/1/` | `200` alice's item | **`404`** `{"detail": "No ReadingListItem matches the given query."}` | none |
| bob: `PATCH /api/reading-list/1/` `{"notes": "hacked"}` | `200`, alice's note changed! | **`404`** | none: notes stay "Chapter 3 next" |
| bob: `POST /api/reading-list/` `{"book": 1, "user": 1}` | `500` IntegrityError (no user) | `201`, `"user": "bob"` (the `"user": 1` in the body is ignored) | new row id 4 with `user_id = 2` |

**Acceptance criteria**
- [ ] `python manage.py test -k task2` → the 3 Task 2 tests pass.
- [ ] You can explain why bob gets **404** (not 403) for alice's item.

---

## Task 3 (STRETCH, optional): Validation rules

> The project milestone practises the same idea (P7-P8), so skip this task if time is short and come back later.

**File:** `catalog/serializers.py`. Find `TODO Task 3a` (`validate_target_date`) and `TODO Task 3b` (`validate_book`).

| Rule | Field | Error message (exact) |
|---|---|---|
| `target_date` cannot be before today (null and today are allowed) | `target_date` | `Target date cannot be in the past.` |
| The current user cannot add a book that is already on **their** list | `book` | `This book is already on your reading list.` |

**Expected input → output** (alice's token; database as above)

| Request | Expected response | Database change |
|---|---|---|
| `POST /api/reading-list/` `{"book": 2, "target_date": "2020-01-01"}` | `400` `{"target_date": ["Target date cannot be in the past."]}` | none |
| `POST /api/reading-list/` `{"book": 1}` | `400` `{"book": ["This book is already on your reading list."]}` | none: alice already has book 1 (item 1) |
| `POST /api/reading-list/` `{"book": 2, "status": "READING"}` | `201` | new row for alice, book 2 |
| `PUT /api/reading-list/1/` `{"book": 1, "status": "FINISHED", "notes": "Done!"}` | `200` (updating an item with **its own** book is fine) | item 1 status → `FINISHED`, notes → `Done!` |
| bob: `POST /api/reading-list/` `{"book": 1}` | `201` (alice has book 1, but bob does not) | new row for bob, book 1 |
| `POST /api/reading-list/` `{"book": 2, "status": "DONE"}` | `400` `{"status": ["\"DONE\" is not a valid choice."]}` (built-in, no code needed) | none |

**Acceptance criteria**
- [ ] `python manage.py test` → `Ran 11 tests ... OK` (all tasks, including this stretch).

---

## Done? Check yourself

- [ ] I can explain the difference between **authentication** (who are you?) and **authorization** (what may you do?).
- [ ] I can explain why `owner`/`user` must never come from the request body.
- [ ] Now apply the same ideas to the project: [`../project-milestone.md`](../project-milestone.md)
