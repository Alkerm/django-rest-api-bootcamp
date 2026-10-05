# Day 4 Project Milestone: Testing, Documentation, Delivery

**Project increment:** at least 8 automated API tests, complete README, dependency file, `.env.example`, settings
from the environment, and a deployment rehearsal.
**Exit check:** all tests pass, a fresh clone can be set up from the README, and the deployment configuration is ready.

## Where to start

- **Finished Day 3?** Continue in your own repository. Copy these from
  [`project/checkpoints/day-04`](../../project/checkpoints/day-04): `tasks/tests.py`, `.env.example`, `.python-version`,
  `requirements.txt`, and `README.md` (replace your short one). Then apply the settings TODO (P3) to your
  `config/settings.py`.
- **Behind?** Copy the whole checkpoint over your project folder (keep `.git` and `.venv`), then
  `python manage.py migrate`.

## TODOs

| TODO | File | What | Hint |
|---|---|---|---|
| P1 | `tasks/tests.py` | read `setUp`, `authenticate()` and the complete example test (no code) | none |
| P2 | `tasks/tests.py` | write the tests that call `self.skipTest(...)`, starting with the two marked *build together with the instructor* | [hints#p2](hints.md#p2) |
| P3 | `config/settings.py` | `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` from environment variables | [hints#p3](hints.md#p3) |
| P4 | `.env.example` | document the three variables with placeholders | [hints#p4](hints.md#p4) |
| P5 | `requirements.txt` | add `psycopg[binary]`, `dj-database-url`, `gunicorn`, `whitenoise` and install them | [hints#p5](hints.md#p5) |
| P6 | `README.md` | complete every `_TODO_` section | [hints#p6](hints.md#p6) |

**Required test coverage** (at least 8 meaningful tests, **none skipped**): unauthenticated access · token login ·
create + owner assignment · own-only list · cross-user access · update · delete · validation.

```bash
python manage.py test          # goal: "Ran 15 tests ... OK" with no "skipped="
```

When a test fails, **fix the application, not the expected result**.

## Peer review: fresh setup from the README

Swap repository URLs with a partner. Each of you, in a **new folder**:

```bash
git clone https://github.com/<partner>/task-management-api.git
```

Follow **only** their README: venv, install, migrate, test, create a user, get a token, create a task.
Write down every step where you had to guess. Give the list to your partner, who fixes the README.

## Deployment rehearsal (prepares tomorrow)

1. Your **Neon** and **Render** accounts open (they were part of the readiness check).
2. In Neon: create a project `tuwaiq-django-api` and find the connection string. **Do not paste it anywhere yet.**
3. In Render: **New → Web Service** → you can see your `task-management-api` repository. Stop before creating it.
4. Read [`setup/deployment.md`](../../setup/deployment.md) once end to end.
5. Locally, run the production checks: they must succeed.

```bash
python -m pip check
python manage.py check
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"   # how you will create SECRET_KEY tomorrow
```

## Commit

```bash
git status                     # .env must NOT be listed
git add .
git commit -m "Day 4: API tests, README, environment configuration"
git push
```

## Exit check

- [ ] Tests cover unauthenticated access, create/owner, own-only list, cross-user access, update, delete, validation.
- [ ] At least 8 meaningful tests pass, with none of the required tests skipped.
- [ ] A partner set up the project from the README without your help.
- [ ] The README documents authentication and every required endpoint with examples.
- [ ] Settings read secrets from the environment; `.env.example` has placeholders only.
- [ ] Neon and Render accounts and the repository connection are verified.
