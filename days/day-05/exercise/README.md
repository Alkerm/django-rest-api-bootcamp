# Day 5 Exercise: Production Readiness (Database Switch, Static Files, Smoke Test)

> **This whole exercise is OPTIONAL (stretch).** Today's priority is deploying **your project**.
> The instructor demonstrates Tasks 1-2 live during the explanation block. Do this exercise only **after** your
> project is deployed and your demo is done, or later as homework. Everything here is also covered by the
> project milestone (P1-P4) and its smoke test.

| | |
|---|---|
| **What you will practice** | Choosing the database from `DATABASE_URL` · serving static files with WhiteNoise when `DEBUG=False` · `collectstatic` · running the app with production-like settings · writing a smoke test that sends real HTTP requests |
| **Where to start** | This folder: `days/day-05/exercise/`. Files: `config/settings.py` (Tasks 1 + 2) → `smoke_test.py` (Task 3) |
| **Result to produce** | The app runs on a database chosen by `DATABASE_URL`, the admin is styled with `DEBUG=False`, and `python smoke_test.py` prints **7/7 checks passed** |
| **Time** | optional: ~45 minutes, after your project is deployed |
| **Hints** | [`../hints.md`](../hints.md) · worked example: [`../example/`](../example/) |

---

## Before you start

Run these in a terminal **opened in this folder** (`days/day-05/exercise`):

```bash
..\..\..\.venv\Scripts\Activate.ps1          # Windows PowerShell
source ../../../.venv/bin/activate            # macOS

python manage.py migrate                      # creates db.sqlite3 (the default database)
python manage.py loaddata sample_data         # -> Installed 14 object(s) from 1 fixture(s)
python manage.py test                         # -> Ran 9 tests ... OK  (the finished Day 4 tests)
```

> **Database state: pre-filled with the Day 3 sample data** (demo users `alice` / `alice-pass-2026` and `bob` /
> `bob-pass-2026`, 6 books, 3 reading-list items). The API is the finished reading-list API. Today you change
> **configuration only**: no views or serializers.

> **Why not Gunicorn locally?** Gunicorn (the production server on Render) does not run on Windows. Locally we use
> `runserver` with `DEBUG=False`, which exercises the same settings.

**Setting environment variables in one terminal** (they last until you close it):

| | Windows PowerShell | macOS |
|---|---|---|
| set | `$env:NAME = "value"` | `export NAME=value` |
| remove | `Remove-Item Env:NAME` | `unset NAME` |

---

## Task 1: Choose the database from `DATABASE_URL`

**File:** `config/settings.py`. Find `TODO [Day 5 · Task 1`.

In production (Render) the database is PostgreSQL on Neon, given as **one** connection string in `DATABASE_URL`.
Locally, without the variable, the project must keep using `db.sqlite3`.

**Verify without installing PostgreSQL.** `dj-database-url` also understands SQLite URLs, so point it at a
*second* SQLite file:

```powershell
$env:DATABASE_URL = "sqlite:///practice.sqlite3"     # macOS: export DATABASE_URL=sqlite:///practice.sqlite3
python manage.py migrate
python manage.py loaddata sample_data
```

| Expected | Database change |
|---|---|
| `migrate` applies all migrations **again**, and a new file `practice.sqlite3` appears in this folder | a brand-new database: same tables, then 14 sample objects |
| `db.sqlite3` is untouched | none |

Optional: if your Neon account is ready, set `DATABASE_URL` to your Neon connection string (keep `?sslmode=require`)
and run `python manage.py migrate`: the same tables are created in PostgreSQL. **Never paste that string into a file.**

**Acceptance criteria**
- [ ] With `DATABASE_URL` set → Django uses that database. Without it → `db.sqlite3`.
- [ ] `python manage.py test` still passes (tests always use a temporary database).

---

## Task 2: Static files with `DEBUG=False`

**File:** `config/settings.py`. Find `TODO Task 2a` (middleware) and `TODO Task 2b` (`STATIC_ROOT` + `STORAGES`).

With `DEBUG=False`, Django stops serving CSS/JS, so the admin and browsable API look broken. WhiteNoise serves them.

```powershell
# keep DATABASE_URL from Task 1 (or remove it), then:
$env:DEBUG = "False"
$env:SECRET_KEY = "any-long-local-test-value-1234567890"
python manage.py collectstatic --noinput     # -> "163 static files copied to ...\staticfiles"
python manage.py runserver
```

**Expected:** http://127.0.0.1:8000/admin/ shows the **styled** login page, and
http://127.0.0.1:8000/static/admin/css/base.css returns CSS (status 200).
Before Task 2 the same page is plain, unstyled HTML (and `collectstatic` fails because `STATIC_ROOT` is missing).

`staticfiles/` is generated output and is ignored by Git.

**Acceptance criteria**
- [ ] `collectstatic` succeeds, and the admin is styled with `DEBUG=False`.

---

## Task 3: Write the smoke test

**File:** `smoke_test.py`. Complete `get_token`, `create_item`, `get_item_status`, `delete_item`
(`TODO Task 3a`-`3d`). `main()` (the scenario) and `list_requires_auth()` (an example) are given.

Keep the server from Task 2 running and use a **second** terminal in this folder:

```bash
python smoke_test.py
```

**Requests it sends and what it expects** (sample data as loaded above):

| # | Request | Expected | Database change |
|---|---|---|---|
| 1 | `GET /api/reading-list/` (no token) | `401` | none |
| 2 | `POST /api/auth/token/` for alice and for bob | `200` + `token` each | token rows created if missing |
| 3 | alice: `POST /api/reading-list/` `{"book": 2}` | `201`, `"user": "alice"` | new reading-list row (alice, book 2) |
| 4 | alice: `GET /api/reading-list/{new id}/` | `200` | none |
| 5 | bob: `GET /api/reading-list/{new id}/` | `404` | none |
| 6 | alice: `DELETE /api/reading-list/{new id}/` | `204` | the new row is removed |
| 7 | alice: `GET /api/reading-list/{new id}/` | `404` | none: the database is back to its starting state |

**Expected output**

```text
Smoke testing http://127.0.0.1:8000
[PASS] 1. GET /api/reading-list/ without token -> 401
...
[PASS] 7. the deleted item is gone -> 404

7/7 checks passed
```

> If check 3 fails with `This book is already on your reading list.`, an earlier run stopped halfway. Delete alice's
> book-2 item in the admin, or reload the sample data (`flush --no-input` + `loaddata sample_data`).

**Acceptance criteria**
- [ ] `python smoke_test.py` prints `7/7 checks passed`.

### Clean up

Close the terminal (or remove `DEBUG`, `SECRET_KEY`, `DATABASE_URL`) and delete `practice.sqlite3` if you like.

---

## Done? Check yourself

- [ ] I can explain why production data cannot live in SQLite on Render (the server's disk is not persistent).
- [ ] I can explain the difference between automated tests (`manage.py test`) and a smoke test.
- [ ] Now deploy your project: [`../project-milestone.md`](../project-milestone.md)
