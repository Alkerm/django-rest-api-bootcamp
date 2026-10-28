# Building REST APIs with Django: Task Management API

**Tuwaiq Club at KFUPM** · Modern Software & Cloud track · October 2026

This repository is **your project**. It contains:

```text
README.md     ← you are here: setup + what to build
HINTS.md      ← step-by-step hints for every TODO
project/      ← the Django project: Day 1 is already done, the TODOs (P1-P10) are what you build
examples/     ← short worked examples (a Movies API) for the same ideas: day-01, day-02, day-03
```

You build a **Task Management API**: CRUD endpoints with one **function view** per operation, a **serializer** that
converts tasks to JSON and validates input, and clear `400` errors for bad data.

---

## 1. Setup (once): run these commands BEFORE the TODOs

**a) Create a NEW, empty repository on GitHub** (for example `task-management-api-final`). Do **not** add a README,
`.gitignore` or license: it must be completely empty. Copy its URL, e.g.
`https://github.com/<your-username>/task-management-api-final.git`.

**b) Open a terminal** in the folder where you keep your work (e.g. your Desktop) and run, in this order:

```powershell
# Windows PowerShell
git clone https://github.com/Alkerm/django-rest-api-bootcamp.git my-task-api     # 1. get the project
cd my-task-api                                                                     # 2. go into it
git remote rename origin bootcamp                                                  # 3. keep the bootcamp as "bootcamp"
git remote add origin https://github.com/<your-username>/<your-new-repo>.git       # 4. YOUR repo becomes "origin"
git push -u origin main                                                            # 5. upload it to your repo
cd project                                                                         # 6. the Django project
py -m venv .venv                                                                   # 7. a fresh environment
.venv\Scripts\Activate.ps1                                                         # 8. activate it
python -m pip install -r requirements.txt                                          # 9. Django + DRF
python manage.py migrate                                                           # 10. create the database
python manage.py createsuperuser                                                   # 11. your admin account
python manage.py runserver                                                         # 12. start the server
```

```bash
# macOS
git clone https://github.com/Alkerm/django-rest-api-bootcamp.git my-task-api     # 1. get the project
cd my-task-api                                                                     # 2. go into it
git remote rename origin bootcamp                                                  # 3. keep the bootcamp as "bootcamp"
git remote add origin https://github.com/<your-username>/<your-new-repo>.git       # 4. YOUR repo becomes "origin"
git push -u origin main                                                            # 5. upload it to your repo
cd project                                                                         # 6. the Django project
python3 -m venv .venv                                                              # 7. a fresh environment
source .venv/bin/activate                                                          # 8. activate it
python -m pip install -r requirements.txt                                          # 9. Django + DRF
python manage.py migrate                                                           # 10. create the database
python manage.py createsuperuser                                                   # 11. your admin account
python manage.py runserver                                                         # 12. start the server
```

**c) Check:** open http://127.0.0.1:8000/admin/ and log in with your superuser. Under **Users → Add user**, create
two normal users, `alice` and `bob` (remember their passwords). Then stop the server with `Ctrl+C`.

You are ready: open `project/` in VS Code and start with **P1**.

> **Problems?** `git push` asks for a password → sign in to GitHub through VS Code or the browser window that opens.
> `Activate.ps1 cannot be loaded` → run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then step 8 again.
> Any other error: show the **exact error text** to a mentor.

Every new terminal: `cd my-task-api/project`, then activate `.venv` (step 8) before running `python manage.py ...`.

---

## 2. What you build: the TODOs

Open each file and look for `TODO [Pn]`. Replace the placeholder line (`# YOUR CODE HERE` and the `pass` / `return`
under it) with your code. Each view answers `501 Not Implemented` until you write it.

| TODO | File | What | Hint |
|---|---|---|---|
| P1 | `tasks/models.py` | `Meta.ordering = ["-created_at"]`, then `python manage.py makemigrations` + `python manage.py migrate` | [P1](HINTS.md#p1) |
| P2 | `tasks/serializers.py` | `fields` (8, in order) and `read_only_fields` (`id`, `owner`, `created_at`, `updated_at`) | [P2](HINTS.md#p2) |
| P3 | `tasks/serializers.py` | clear title errors: `Title is required.` / `Title cannot be blank.` | [P3](HINTS.md#p3) |
| P4 | `tasks/serializers.py` | `validate_due_date`: not before today, **on create only** | [P4](HINTS.md#p4) |
| P5 | `tasks/views.py` | `list_tasks` and `get_task` return `TaskSerializer(...).data` | [P5](HINTS.md#p5) |
| P6 | `tasks/views.py` | `create_task`: `is_valid()` → 400, or `save(owner=request.user)` → 201 | [P6](HINTS.md#p6) |
| P7 | `tasks/views.py` | `update_task`: `partial` for PATCH, 400 on invalid input | [P7](HINTS.md#p7) |
| P8 | `tasks/views.py` | `delete_task` → 204 | [P8](HINTS.md#p8) |
| P9 | `tasks/urls.py` | five `path()` routes, names `task-list` … `task-delete` | [P9](HINTS.md#p9) |
| P10 | `config/urls.py` | include `tasks.urls` under `api/` and DRF login under `api-auth/` | [P10](HINTS.md#p10) |
| P11 *(stretch)* | `tasks/serializers.py` | show `owner` as the username | [P11](HINTS.md#p11) |

**Suggested order:** P1 → P2-P4 (serializer) → P5-P8 (views) → P9-P10 (URLs). Nothing is reachable in the browser
until P9 and P10 are done, so do them as soon as you have written your first view if you want to try things early.

### The URLs you are building

| Operation | Method + URL | View | Success | Typical failures |
|---|---|---|---|---|
| list | `GET /api/tasks/` | `list_tasks` | 200 + list | none |
| create | `POST /api/tasks/create/` | `create_task` | 201 + task | 400 invalid body |
| retrieve | `GET /api/tasks/{id}/` | `get_task` | 200 + task | 404 unknown id |
| update | `PUT` / `PATCH /api/tasks/{id}/update/` | `update_task` | 200 + task | 400, 404 |
| delete | `DELETE /api/tasks/{id}/delete/` | `delete_task` | 204, empty body | 404 |

A wrong method on a URL (for example `DELETE /api/tasks/3/`) returns **405 Method Not Allowed**.

---

## 3. Try it

```bash
python manage.py runserver
```

1. Log in at http://127.0.0.1:8000/api-auth/login/ as `alice`.
2. Open each URL in the browser. Every page has a form at the bottom to send JSON (choose `application/json`); the
   delete page has a red **DELETE** button.

| # | Request | Body | Expected |
|---|---|---|---|
| 1 | `GET /api/tasks/` | none | `200`, list newest first |
| 2 | `POST /api/tasks/create/` | `{"title": "Prepare slides", "owner": 999}` | `201`, owner = alice (999 ignored) |
| 3 | `GET /api/tasks/{id}/` | none | `200` |
| 4 | `PUT /api/tasks/{id}/update/` | `{"status": "DONE"}` | `400`: PUT needs the title |
| 5 | `PATCH /api/tasks/{id}/update/` | `{"status": "DONE"}` | `200`, only status changed |
| 6 | `POST /api/tasks/create/` | `{"title": "   "}` | `400` `{"title": ["Title cannot be blank."]}` |
| 7 | `POST /api/tasks/create/` | `{"description": "no title"}` | `400` `{"title": ["Title is required."]}` |
| 8 | `POST /api/tasks/create/` | `{"title": "X", "status": "FINISHED"}` | `400`, error on `status` |
| 9 | `POST /api/tasks/create/` | `{"title": "X", "due_date": "2020-01-01"}` | `400` `{"due_date": ["Due date cannot be earlier than today."]}` |
| 10 | `DELETE /api/tasks/{id}/delete/` | none | `204`; a GET on the same id then gives `404` |
| 11 | `DELETE /api/tasks/{id}/` | none | `405` (wrong URL for delete) |

Check the database after each write (admin or DB Browser).

> **Known gap:** every logged-in user sees **all** users' tasks. Making each user see only their own tasks (token
> authentication and ownership) is the next step after this bootcamp: see `examples/` and the DRF docs.

---

## 4. Save your work (do this often)

```bash
git add .
git commit -m "Task API: CRUD with function views and a serializer"
git push
```

`git push` goes to **your** repository (`origin`). The bootcamp repository is still available as `bootcamp` if the
instructors announce an update: `git pull bootcamp main`.

## Done? Check yourself

- [ ] All five URLs work with the expected status codes; a wrong method gives `405`.
- [ ] Create returns `201`, the row appears in the database, and the owner is set by the server.
- [ ] PUT without a title returns `400`; PATCH with one field returns `200`.
- [ ] Blank or missing title, invalid status, and a past due date on create return `400` with field errors.
- [ ] All eleven checks above pass and your work is pushed to **your** repository.

## Stack

Python 3.13 · Django 5.2 LTS · Django REST Framework 3.16 · SQLite + DB Browser · Git + GitHub.
