# Day 3 Project Milestone: Serialization and Validation

**Project increment:** `TaskSerializer`, the five views rewritten with it, and the validation rules.
**Exit check:** all CRUD operations still work, and invalid input returns `400` with clear field-level errors.

## Where to start

**Combined session (Tuesday):** copy this checkpoint as soon as you finish the Day 2 TODOs, or when the instructor
moves on to Day 3, whichever comes first. It replaces your Day 2 files with the solved version:

```powershell
# Windows PowerShell
git -C django-rest-api-bootcamp pull
cd task-management-api
git add -A; git commit -m "End of Day 2"
Copy-Item -Path ..\django-rest-api-bootcamp\project\checkpoints\day-03\* -Destination . -Recurse -Force
.venv\Scripts\Activate.ps1
python manage.py migrate
```

```bash
# macOS
git -C django-rest-api-bootcamp pull
cd task-management-api
git add -A && git commit -m "End of Day 2"
cp -R ../django-rest-api-bootcamp/project/checkpoints/day-03/. .
source .venv/bin/activate
python manage.py migrate
```

The checkpoint adds a new file, `tasks/serializers.py`, and replaces `task_to_dict` in `tasks/views.py`. The URLs do
not change.

## TODOs

| TODO | File | What | Hint |
|---|---|---|---|
| P1 | `tasks/serializers.py` | `fields` (the 8 from `task_to_dict`) and `read_only_fields` (`id`, `owner`, `created_at`, `updated_at`) | [hints#p1](hints.md#p1) |
| P2 | `tasks/views.py` | `list_tasks` and `get_task` return `TaskSerializer(...).data` | [hints#p2](hints.md#p2) |
| P3 | `tasks/views.py` | `create_task`: `is_valid()` → 400, or `save(owner=request.user)` → 201 | [hints#p3](hints.md#p3) |
| P4 | `tasks/views.py` | `update_task`: `partial` for PATCH, 400 on invalid input | [hints#p4](hints.md#p4) |
| P5 | `tasks/serializers.py` | clear title errors: `Title is required.` / `Title cannot be blank.` | [hints#p5](hints.md#p5) |
| P6 | `tasks/serializers.py` | `validate_due_date`: not before today, **on create only** | [hints#p6](hints.md#p6) |
| P7 *(stretch)* | `tasks/serializers.py` | show `owner` as the username instead of the id | [hints#p7](hints.md#p7) |

## Try it

```bash
python manage.py runserver
```

Log in at http://127.0.0.1:8000/api-auth/login/ as `alice`, then:

| # | Request | Body | Expected |
|---|---|---|---|
| 1 | `GET /api/tasks/` | none | `200`, the same JSON shape as yesterday |
| 2 | `POST /api/tasks/create/` | `{"title": "Prepare slides", "owner": 999}` | `201`, owner = alice (999 ignored) |
| 3 | `POST /api/tasks/create/` | `{"title": "   "}` | `400` `{"title": ["Title cannot be blank."]}` |
| 4 | `POST /api/tasks/create/` | `{"description": "no title"}` | `400` `{"title": ["Title is required."]}` |
| 5 | `POST /api/tasks/create/` | `{"title": "X", "status": "FINISHED"}` | `400`, error on `status` (built-in, no code needed) |
| 6 | `POST /api/tasks/create/` | `{"title": "X", "due_date": "2020-01-01"}` | `400` `{"due_date": ["Due date cannot be earlier than today."]}` |
| 7 | `POST /api/tasks/create/` | `{"title": "X", "due_date": "tomorrow"}` | `400`, error on `due_date` (Day 2: 500) |
| 8 | `PUT /api/tasks/{id}/update/` | `{"status": "DONE"}` | `400`: PUT needs the title |
| 9 | `PATCH /api/tasks/{id}/update/` | `{"status": "DONE"}` | `200`, only status changed |
| 10 | `DELETE /api/tasks/{id}/delete/` | none | `204` |

> **Known gap, fixed on Day 4:** every logged-in user still sees **all** users' tasks. Day 4 adds token
> authentication and per-user isolation.

## Commit

```bash
git add .
git commit -m "Day 3: TaskSerializer and validation"
git push
```

## Exit check

- [ ] No view builds a dict by hand; every view uses `TaskSerializer`.
- [ ] `owner`, `id`, `created_at`, `updated_at` are read-only; the owner is set by the server.
- [ ] Blank or missing title, invalid status, and a past due date on create return `400` with field errors.
- [ ] PUT without a title returns `400`; PATCH with one field returns `200`.
- [ ] All ten checks above pass and the commit is pushed.
