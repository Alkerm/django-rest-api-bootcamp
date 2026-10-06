# Day 4 Project Milestone: Testing and Configuration

**Project increment:** at least 8 automated API tests, settings from the environment, `.env.example`, and the
deployment packages in `requirements.txt`. (The README is completed on Day 5.)
**Exit check:** all required tests pass, settings come from the environment, and the dependency file is ready for deployment.

## Where to start

**Everyone does the same thing each morning:** copy today's checkpoint over your project. It contains everything up
to yesterday already solved, plus today's TODOs, so you never have to merge files by hand. Your Git history, your
`.venv` and your database (users and tasks) are kept.

Open a terminal in the folder that contains **both** `django-rest-api-bootcamp` and `task-management-api`:

```powershell
# Windows PowerShell
git -C django-rest-api-bootcamp pull       # only when the instructor announces an update
cd task-management-api
git add -A; git commit -m "End of Day 3"                       # save your own work first
Copy-Item -Path ..\django-rest-api-bootcamp\project\checkpoints\day-04\* -Destination . -Recurse -Force
.venv\Scripts\Activate.ps1
python manage.py migrate
```

```bash
# macOS
git -C django-rest-api-bootcamp pull       # only when the instructor announces an update
cd task-management-api
git add -A && git commit -m "End of Day 3"
cp -R ../django-rest-api-bootcamp/project/checkpoints/day-04/. .
source .venv/bin/activate
python manage.py migrate
```

> Curious how your Day 3 code compares with the reference? Run `git diff` before your next commit: the differences
> are a free code review. `nothing to commit` after `git commit` is fine.

## TODOs

| TODO | File | What | Hint |
|---|---|---|---|
| P1 | `tasks/tests.py` | read `setUp`, `authenticate()` and the complete example test (no code) | none |
| P2 | `tasks/tests.py` | write the 7 tests marked **REQUIRED**, starting with the two marked *build together with the instructor*. The 7 **STRETCH** tests are optional | [hints#p2](hints.md#p2) |
| P3 | `config/settings.py` | `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` from environment variables | [hints#p3](hints.md#p3) |
| P4 | `.env.example` | document the three variables with placeholders | [hints#p4](hints.md#p4) |
| P5 | `requirements.txt` | add `psycopg[binary]`, `dj-database-url`, `gunicorn`, `whitenoise`, then `python -m pip install -r requirements.txt` | [hints#p5](hints.md#p5) |

**Required test coverage** = the example + the 7 REQUIRED tests (8 in total): unauthenticated access · token login ·
create + owner assignment · own-only list · cross-user access · update · delete · validation.

```bash
python manage.py test          # goal: "OK (skipped=7)": only STRETCH tests may still be skipped
python manage.py test -v 2     # shows which tests are still skipped, and whether each is REQUIRED or STRETCH
```

Finish P3-P5 **before** any STRETCH test.

When a test fails, **fix the application, not the expected result**.

## Homework (optional, ~15 minutes): get ready for Day 5

Day 5 is deployment day. Arriving with these done makes it much smoother:

1. Your **Neon** and **Render** accounts open (they were part of the readiness check).
2. In Neon: create a project `tuwaiq-django-api` and find the connection string. **Do not paste it anywhere yet.**
3. In Render: **New → Web Service** → you can see your `task-management-api` repository. Stop before creating it.
4. Read [`setup/deployment.md`](../../setup/deployment.md) once end to end.

The README you received today (template with `_TODO_` sections) is completed on **Day 5**. If you want a head start,
fill in the sections you already know (setup, tests, authentication).

## Commit

```bash
git status                     # .env must NOT be listed
git add .
git commit -m "Day 4: API tests and environment configuration"
git push
```

## Exit check

- [ ] Tests cover unauthenticated access, create/owner, own-only list, cross-user access, update, delete, validation.
- [ ] At least 8 meaningful tests pass (the example + 7 REQUIRED); only STRETCH tests may be skipped.
- [ ] Settings read secrets from the environment; `.env.example` has placeholders only.
- [ ] `python -m pip check` reports no broken requirements.
