# Day 2 Project Milestone: Core API (Complete CRUD)

**Project increment:** serializer, viewset, router, and the six CRUD operations at `/api/tasks/`.
**Exit check:** all CRUD operations work locally with valid JSON and appropriate status codes.

## Where to start

- **Finished Day 1?** Continue in your own `task-management-api` repository.
- **Behind?** Copy the files of [`project/checkpoints/day-02`](../../project/checkpoints/day-02) over your project
  folder (keep your `.git` and `.venv` folders). It contains Day 1 solved + today's TODOs.
  Then run `python manage.py migrate` and make sure you have two users and a superuser.

> If you continue your own project: create these new files by copying them from `project/checkpoints/day-02/`:
> `tasks/serializers.py`, `tasks/views.py`, `tasks/urls.py`. Then copy the `REST_FRAMEWORK` block at the end of
> `config/settings.py`, and replace `config/urls.py`. They contain today's TODOs.

## TODOs

| TODO | File | What | Hint |
|---|---|---|---|
| P1 *(Day 1 review)* | `tasks/models.py` | `Meta.ordering = ["-created_at"]` + `makemigrations` + `migrate` | [hints#p1](hints.md#p1) |
| P2 | `tasks/serializers.py` | `fields` (all 8) and `read_only_fields` (`id`, `owner`, `created_at`, `updated_at`) | [hints#p2](hints.md#p2) |
| P3 | `tasks/views.py` | `queryset` + `serializer_class` | [hints#p3](hints.md#p3) |
| P4 | `tasks/views.py` | `perform_create` → owner = logged-in user | [hints#p4](hints.md#p4) |
| P5 | `tasks/urls.py` | register `TaskViewSet` as `tasks`, `basename="task"` | [hints#p5](hints.md#p5) |
| P6 | `config/urls.py` | include `tasks.urls` under `api/` and DRF login under `api-auth/` | [hints#p6](hints.md#p6) |

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

Check the database after each write (admin or DB Browser).

> **Known gap, fixed tomorrow:** today every logged-in user sees **all** users' tasks. Day 3 adds token
> authentication and per-user isolation.

## Commit

```bash
git add .
git commit -m "Day 2: Task serializer, viewset, router, CRUD endpoints"
git push
```

## Exit check

- [ ] List and detail routes resolve without writing URLs by hand (router).
- [ ] Create returns `201` and the row appears in the database.
- [ ] Retrieve returns `200`; an unknown id returns `404`.
- [ ] PUT/PATCH change the intended fields; DELETE returns `204`.
- [ ] `owner` is read-only and assigned by the server.
- [ ] All seven checks above pass and the commit is pushed.
