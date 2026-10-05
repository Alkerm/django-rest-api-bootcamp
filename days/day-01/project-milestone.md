# Day 1 Project Milestone: Foundation

**Project increment:** repository, Django/DRF project, `tasks` app, `Task` model, migrations, admin data.
**Exit check:** the repository is pushed, the server starts locally, and the admin shows saved Task records after a restart.

Do this **after** the exercise. You use exactly the same skills on the real project.

---

## 1. Create your own project from the starter

Your project lives in **its own folder and its own GitHub repository** (`task-management-api`), **outside** this
bootcamp repository.

```powershell
# Windows PowerShell - run from the folder that CONTAINS the bootcamp repository
Copy-Item -Recurse django-rest-api-bootcamp\project\starter task-management-api
cd task-management-api
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

```bash
# macOS
cp -R django-rest-api-bootcamp/project/starter task-management-api
cd task-management-api
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

The starter is what `django-admin startproject config .` and `python manage.py startapp tasks` generate, with comments
and TODOs added. Look around first: `config/` holds **project** settings and URLs, while `tasks/` is the **app** that
owns task behaviour.

## 2. Complete the TODOs

| TODO | File | What | Hint |
|---|---|---|---|
| P1 | `config/settings.py` | register `rest_framework` and `tasks` in `INSTALLED_APPS` | [hints#p1](hints.md#p1) |
| P2 | `tasks/models.py` | `Status` choices: `TODO`, `IN_PROGRESS`, `DONE` | [hints#p2](hints.md#p2) |
| P3 | `tasks/models.py` | fields `title`, `description`, `status`, `due_date`, `owner`, `created_at`, `updated_at` | [hints#p3](hints.md#p3) |
| P4 | `tasks/models.py` | `__str__` → `"Buy groceries (To do)"` | [hints#p4](hints.md#p4) |
| P5 | `tasks/admin.py` | register `Task` with columns, filters, search | [hints#p5](hints.md#p5) |

**The `Task` table you are building** (`tasks_task`):

| Field | Type | Rules |
|---|---|---|
| `id` | BigAutoField | automatic |
| `title` | CharField(200) | required |
| `description` | TextField | optional (`blank=True`) |
| `status` | CharField(20) | `TODO` (default) / `IN_PROGRESS` / `DONE` |
| `due_date` | DateField | optional (`null=True, blank=True`) |
| `owner` | ForeignKey → User | `CASCADE`, `related_name="tasks"` |
| `created_at` | DateTimeField | `auto_now_add=True` |
| `updated_at` | DateTimeField | `auto_now=True` |

## 3. Build the database and add data

```bash
python manage.py makemigrations tasks     # -> tasks/migrations/0001_initial.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver                # http://127.0.0.1:8000/admin/
```

In the admin, create **two users** (e.g. `alice`, `bob`; remember the passwords, you need them on Day 3) and
**at least 3 tasks** with different owners and statuses. Stop the server (Ctrl+C), start it again: the tasks are still
there.

## 4. Push to GitHub

1. On GitHub create an **empty** repository named `task-management-api` (no README, no .gitignore, no license).
2. Check that `.gitignore` is present (it came with the starter), then:

```bash
git init
git status                     # .venv/ and db.sqlite3 must NOT be listed
git add .
git commit -m "Day 1: Django project, Task model, admin"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/task-management-api.git
git push -u origin main
```

## Exit check

- [ ] A fresh terminal can activate `.venv` and start the server.
- [ ] `python manage.py migrate` reports **No migrations to apply**.
- [ ] Task fields and status choices match the table above.
- [ ] The admin creates, edits and keeps Task records with owners after a restart.
- [ ] The repository is on GitHub **without** `.venv/`, `db.sqlite3`, or any secret.

**Fell behind?** Tomorrow you can start from [`project/checkpoints/day-02`](../../project/checkpoints/day-02), which
contains everything from today, already solved.
