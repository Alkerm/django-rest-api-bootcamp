# Day 2 Project Milestone: Core API (CRUD with Function Views)

**Project increment:** five function views (list, create, retrieve, update, delete), five URLs under `/api/tasks/`,
and the owner set by the server.
**Exit check:** all CRUD operations work locally with valid JSON and the right status codes; a blank title returns
`400`.

> **Combined session (Tuesday):** today you do the Day 2 TODOs, then continue with
> [Day 3](../day-03/project-milestone.md) in the same session. Not finished with Day 2 when the instructor moves on?
> That is fine: the `day-03` checkpoint has Day 2 already solved.

## Where to start

**Everyone does the same thing each morning:** copy today's checkpoint over your project. It contains everything up
to yesterday already solved, plus today's TODOs, so you never have to merge files by hand. Your Git history, your
`.venv` and your database (users and tasks) are kept.

Open a terminal in the folder that contains **both** `django-rest-api-bootcamp` and `task-management-api`:

```powershell
# Windows PowerShell
git -C django-rest-api-bootcamp pull       # only when the instructor announces an update
cd task-management-api
git add -A; git commit -m "End of Day 1"                       # save your own work first
Copy-Item -Path ..\django-rest-api-bootcamp\project\checkpoints\day-02\* -Destination . -Recurse -Force
.venv\Scripts\Activate.ps1
python manage.py migrate
```

```bash
# macOS
git -C django-rest-api-bootcamp pull       # only when the instructor announces an update
cd task-management-api
git add -A && git commit -m "End of Day 1"
cp -R ../django-rest-api-bootcamp/project/checkpoints/day-02/. .
source .venv/bin/activate
python manage.py migrate
```

> **Did your Day 1 model differ from the field table** (e.g. `due_date` without `null=True`)? Then your database
> was built from a different migration than the checkpoint's, and creating a task can fail later with an error such as
> `NOT NULL constraint failed`. Fix it now, it takes 2 minutes: delete `db.sqlite3`, run `python manage.py migrate`,
> then recreate your superuser (`createsuperuser`) and `alice` / `bob` in the admin.

> Curious how your Day 1 code compares with the reference? Run `git diff` before your next commit: the differences
> are a free code review. `nothing to commit` after `git commit` is fine.

## TODOs

| TODO | File | What | Hint |
|---|---|---|---|
| P1 *(Day 1 review)* | `tasks/models.py` | `Meta.ordering = ["-created_at"]` + `makemigrations` + `migrate` | [hints#p1](hints.md#p1) |
| P2 | `tasks/views.py` | `task_to_dict`: the 8 API fields, `owner` as its id | [hints#p2](hints.md#p2) |
| P3 | `tasks/views.py` | `list_tasks` + `create_task` (blank title → 400, owner = logged-in user) | [hints#p3](hints.md#p3) |
| P4 | `tasks/views.py` | `get_task` (unknown id → 404) | [hints#p4](hints.md#p4) |
| P5 | `tasks/views.py` | `update_task`: change only the fields that were sent | [hints#p5](hints.md#p5) |
| P6 | `tasks/views.py` | `delete_task` → 204 | [hints#p6](hints.md#p6) |
| P7 | `tasks/urls.py` | five `path()` routes with the names `task-list` … `task-delete` | [hints#p7](hints.md#p7) |
| P8 | `config/urls.py` | include `tasks.urls` under `api/` and DRF login under `api-auth/` | [hints#p8](hints.md#p8) |

Each view answers `501 Not Implemented` until you replace its placeholder line.

## Try it

```bash
python manage.py runserver
```

1. Log in at http://127.0.0.1:8000/api-auth/login/ as `alice` (today's temporary login; tokens come on Day 4).
2. Open http://127.0.0.1:8000/api/tasks/ and work through the checklist:

| # | Request | Body | Expected |
|---|---|---|---|
| 1 | `GET /api/tasks/` | none | `200`, list newest first |
| 2 | `POST /api/tasks/create/` | `{"title": "Prepare slides", "status": "TODO", "owner": 999}` | `201`, `owner` = alice's id (999 ignored) |
| 3 | `GET /api/tasks/{id}/` | none | `200` |
| 4 | `PUT /api/tasks/{id}/update/` | `{"title": "Prepare final slides", "description": "", "status": "IN_PROGRESS", "due_date": null}` | `200`, fields changed |
| 5 | `PATCH /api/tasks/{id}/update/` | `{"status": "DONE"}` | `200`, only status changed |
| 6 | `DELETE /api/tasks/{id}/delete/` | none | `204` |
| 7 | `GET /api/tasks/{id}/` (deleted id) | none | `404` |
| 8 | `POST /api/tasks/create/` | `{"title": "   "}` | `400` `{"title": ["Title is required."]}` |
| 9 | `DELETE /api/tasks/{id}/` | none | `405` (wrong URL for delete) |

Check the database after each write (admin or DB Browser).

> **Known gaps, fixed in the next days:**
> - Send `{"title": "X", "status": "FINISHED"}`: it is **saved**, although `FINISHED` is not a valid status. A date
>   like `"due_date": "tomorrow"` even crashes with a 500. **Day 3** adds a serializer that validates every field.
> - Every logged-in user sees **all** users' tasks. **Day 4** adds token authentication and per-user isolation.

## Commit

```bash
git add .
git commit -m "Day 2: Task CRUD with function views and path() routes"
git push
```

## Exit check

- [ ] Each of the five URLs reaches its view (wrong method → `405`).
- [ ] Create returns `201` and the row appears in the database.
- [ ] Retrieve returns `200`; an unknown id returns `404`.
- [ ] PUT/PATCH change only the intended fields; DELETE returns `204`.
- [ ] `owner` is assigned by the server, never taken from the request body.
- [ ] A blank title returns `400` and saves nothing.
- [ ] All nine checks above pass and the commit is pushed.
