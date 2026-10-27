# Day 4 Project Milestone: Security and Configuration

**Project increment:** token login endpoint, protected routes, per-user isolation in every view, cross-user
protection, and settings read from environment variables.
**Exit check:** user A cannot view or modify user B's tasks, requests without a token get `401`, and the project's
configuration comes from the environment.

## Step 0: run these commands BEFORE you start the TODOs

**This is the last copy of the bootcamp.** The `day-04` checkpoint is the **final** one: Days 1-3 solved, plus every
TODO for Day 4 and Day 5. Copy it once now and keep working in the same project until the end. Your Git history, your
`.venv` and your database (users and tasks) are kept.

Open a terminal in the folder that contains **both** `django-rest-api-bootcamp` and `task-management-api`, then run
these lines **in this order**:

```powershell
# Windows PowerShell
git -C django-rest-api-bootcamp pull                     # 1. get the final checkpoint
cd task-management-api                                   # 2. go into YOUR project
git add -A; git commit -m "End of Day 3"                 # 3. save your own work first
Copy-Item -Path ..\django-rest-api-bootcamp\project\checkpoints\day-04\* -Destination . -Recurse -Force   # 4. copy
.venv\Scripts\Activate.ps1                               # 5. activate your environment
python manage.py migrate                                 # 6. update the database
python manage.py runserver                               # 7. check it starts, then stop it with Ctrl+C
```

```bash
# macOS
git -C django-rest-api-bootcamp pull                     # 1. get the final checkpoint
cd task-management-api                                   # 2. go into YOUR project
git add -A && git commit -m "End of Day 3"               # 3. save your own work first
cp -R ../django-rest-api-bootcamp/project/checkpoints/day-04/. .   # 4. copy
source .venv/bin/activate                                # 5. activate your environment
python manage.py migrate                                 # 6. update the database
python manage.py runserver                               # 7. check it starts, then stop it with Ctrl+C
```

**Step 7 shows `Starting development server at http://127.0.0.1:8000/`? You are ready: start with P1.**
`nothing to commit` in step 3 is fine. If a step fails, stop and show the exact error to a mentor.

**One more command later:** right after **P1** (adding `rest_framework.authtoken`), run `python manage.py migrate`
again: it creates the token table (`Applying authtoken...`).

The checkpoint also brings new files: `.env.example`, `.python-version`, `smoke_test.py`, and a **README template**
that you complete on Day 5 (`TODO [Day 5 · P1]` in `README.md`).

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

Do Part 1 and the two-user check first; Part 2 is short.

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

Save evidence (screenshots or copied responses, **without tokens**) in your notes. On Day 5 the smoke test runs the same
checks automatically.

## Configuration check

```bash
python manage.py runserver        # still works with NO variables set (development defaults)
git status                        # .env must NOT be listed
```

## Head start on Day 5

The README you received today (template with `_TODO_` sections) is completed on **Day 5**. If you have time, fill in
the sections you already know (setup, authentication).

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
- [ ] Settings read secrets from the environment; `.env.example` has placeholders only.
- [ ] The two-user check is recorded and the commit is pushed.
