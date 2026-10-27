# Day 4 Project Milestone: Security and Configuration

**Project increment:** token login endpoint, protected routes, per-user isolation in every view, cross-user
protection; settings from environment variables and the deployment packages for Day 5.
**Exit check:** user A cannot view or modify user B's tasks, requests without a token get `401`, and the project's
configuration comes from the environment.

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

The checkpoint also brings new files: `.env.example`, `.python-version`, and a **README template** that you complete
on Day 5.

## TODOs

### Part 1: Security (~40 min)

| TODO | File | What | Hint |
|---|---|---|---|
| P1 | `config/settings.py` | add `rest_framework.authtoken`, then `migrate` | [hints#p1](hints.md#p1) |
| P2 | `config/settings.py` | `DEFAULT_AUTHENTICATION_CLASSES`: Token first, then Session | [hints#p2](hints.md#p2) |
| P3 | `config/urls.py` | import `obtain_auth_token`, add `api/auth/token/` (`name="api-token"`) | [hints#p3](hints.md#p3) |
| P4 | `tasks/views.py` | `list_tasks` → only the caller's tasks | [hints#p4](hints.md#p4) |
| P5 | `tasks/views.py` | `get_own_task()` → look up by id **and** owner (used by get, update, delete) | [hints#p5](hints.md#p5) |

### Part 2: Configuration (~15 min)

| TODO | File | What | Hint |
|---|---|---|---|
| P6 | `config/settings.py` | `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` from environment variables | [hints#p6](hints.md#p6) |
| P7 | `.env.example` | document the three variables with placeholders | [hints#p7](hints.md#p7) |
| P8 | `requirements.txt` | add `psycopg[binary]`, `dj-database-url`, `gunicorn`, `whitenoise`, then `python -m pip install -r requirements.txt` | [hints#p8](hints.md#p8) |

Do Part 1 and the two-user check first; Part 2 is short and is needed for the deployment later in the same session
(Day 5).

## The two-user security check (record the results)

Use Postman (see [`setup/postman.md`](../../setup/postman.md)) with the two users you created on Day 1.
Make sure **each** user owns at least one task (use the admin if needed).

| # | Request | Expected |
|---|---|---|
| 1 | `POST /api/auth/token/` alice's credentials | `200` + token |
| 2 | `POST /api/auth/token/` wrong password | `400` |
| 3 | `GET /api/tasks/` **without** token | `401` |
| 4 | alice: `GET /api/tasks/` | `200`, only alice's tasks |
| 5 | alice: `POST /api/tasks/create/` `{"title": "Mine", "owner": <bob's id>}` | `201`, owner is alice |
| 6 | bob: `GET /api/tasks/{alice's task id}/` | `404` |
| 7 | bob: `PATCH /api/tasks/{alice's task id}/update/` `{"title": "x"}` | `404`, alice's task unchanged |
| 8 | bob: `DELETE /api/tasks/{alice's task id}/delete/` | `404`, task still exists |

Save evidence (screenshots or copied responses, **without tokens**) in your notes. On Day 5 you run the same checks
against your live URL.

## Configuration check

```bash
python manage.py runserver        # still works with NO variables set (development defaults)
python -m pip check               # "No broken requirements found."
git status                        # .env must NOT be listed
```

## Before Wednesday's session (strongly recommended, ~15 minutes): get ready for deployment

Day 4 and Day 5 share one session, so there is little time to set up accounts. Arrive with these done:

1. Your **Neon** and **Render** accounts open (they were part of the readiness check).
2. In Neon: create a project `tuwaiq-django-api` and find the connection string. **Do not paste it anywhere yet.**
3. In Render: **New → Web Service** → you can see your `task-management-api` repository. Stop before creating it.
4. Read [`setup/deployment.md`](../../setup/deployment.md) once end to end.

The README you received today (template with `_TODO_` sections) is completed on **Day 5**. If you want a head start,
fill in the sections you already know (setup, authentication).

## Commit

```bash
git status                     # .env must NOT be listed
git add .
git commit -m "Day 4: token auth, ownership, environment configuration"
git push
```

## Exit check

- [ ] Valid credentials return a token; protected routes reject requests without one (`401`).
- [ ] Authenticated creation ignores any client-supplied owner.
- [ ] Each user's list contains only their own records.
- [ ] Cross-user retrieve/update/delete is blocked (`404`) without leaking data.
- [ ] Settings read secrets from the environment; `.env.example` has placeholders only; `pip check` is clean.
- [ ] The two-user check is recorded and the commit is pushed.
