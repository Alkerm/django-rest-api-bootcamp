# Day 2 Project Milestone: Core API (Complete CRUD + Validation)

**Project increment:** serializer, viewset, router, the six CRUD operations at `/api/tasks/`, and input validation.
**Exit check:** all CRUD operations work locally with valid JSON and appropriate status codes, and invalid input
returns `400` with clear field-level errors.

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

> Curious how your Day 1 code compares with the reference? Run `git diff` before your next commit: the differences
> are a free code review. `nothing to commit` after `git commit` is fine.

## TODOs

| TODO | File | What | Hint |
|---|---|---|---|
| P1 *(Day 1 review)* | `tasks/models.py` | `Meta.ordering = ["-created_at"]` + `makemigrations` + `migrate` | [hints#p1](hints.md#p1) |
| P2 | `tasks/serializers.py` | `fields` (all 8) and `read_only_fields` (`id`, `owner`, `created_at`, `updated_at`) | [hints#p2](hints.md#p2) |
| P3 | `tasks/views.py` | `queryset` + `serializer_class` | [hints#p3](hints.md#p3) |
| P4 | `tasks/views.py` | `perform_create` → owner = logged-in user | [hints#p4](hints.md#p4) |
| P5 | `tasks/urls.py` | register `TaskViewSet` as `tasks`, `basename="task"` | [hints#p5](hints.md#p5) |
| P6 | `config/urls.py` | include `tasks.urls` under `api/` and DRF login under `api-auth/` | [hints#p6](hints.md#p6) |
| P7 | `tasks/serializers.py` | clear title errors: `Title is required.` / `Title cannot be blank.` | [hints#p7](hints.md#p7) |
| P8 | `tasks/serializers.py` | `validate_due_date`: not before today, **on create only** | [hints#p8](hints.md#p8) |

## Try it

```bash
python manage.py runserver
```

1. Log in at http://127.0.0.1:8000/api-auth/login/ as `alice` (today's temporary login; tokens come on Day 3).
2. Open http://127.0.0.1:8000/api/tasks/ and work through the checklist:

| # | Request | Body | Expected |
|---|---|---|---|
| 1 | `GET /api/tasks/` | none | `200`, list newest first |
| 2 | `POST /api/tasks/` | `{"title": "Prepare slides", "status": "TODO", "owner": 999}` | `201`, `owner` = alice's id (999 ignored) |
| 3 | `GET /api/tasks/{id}/` | none | `200` |
| 4 | `PUT /api/tasks/{id}/` | `{"title": "Prepare final slides", "description": "", "status": "IN_PROGRESS", "due_date": null}` | `200`, all fields replaced |
| 5 | `PATCH /api/tasks/{id}/` | `{"status": "DONE"}` | `200`, only status changed |
| 6 | `DELETE /api/tasks/{id}/` | none | `204` |
| 7 | `GET /api/tasks/{id}/` (deleted id) | none | `404` |
| 8 | `POST /api/tasks/` | `{"title": "   "}` | `400` `{"title": ["Title cannot be blank."]}` |
| 9 | `POST /api/tasks/` | `{"title": "X", "status": "FINISHED"}` | `400`, error on `status` (built-in, no code needed) |
| 10 | `POST /api/tasks/` | `{"title": "X", "due_date": "2020-01-01"}` | `400` `{"due_date": ["Due date cannot be earlier than today."]}` |

Check the database after each write (admin or DB Browser).

> **Known gap, fixed tomorrow:** today every logged-in user sees **all** users' tasks. Day 3 adds token
> authentication and per-user isolation.

## Commit

```bash
git add .
git commit -m "Day 2: Task serializer, viewset, router, CRUD endpoints, validation"
git push
```

## Exit check

- [ ] List and detail routes resolve without writing URLs by hand (router).
- [ ] Create returns `201` and the row appears in the database.
- [ ] Retrieve returns `200`; an unknown id returns `404`.
- [ ] PUT/PATCH change the intended fields; DELETE returns `204`.
- [ ] `owner` is read-only and assigned by the server.
- [ ] Blank title, invalid status, and a past due date on create return `400` with field errors.
- [ ] All ten checks above pass and the commit is pushed.
