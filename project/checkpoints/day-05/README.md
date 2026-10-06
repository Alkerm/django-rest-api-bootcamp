# Task Management API

A personal task management REST API built with **Django 5.2** and **Django REST Framework 3.16**.
Each authenticated user creates and manages **only their own tasks**: the API validates input, protects every task
endpoint with token authentication, and blocks access to other users' data.

Built during the Tuwaiq Club at KFUPM bootcamp *Building REST APIs with Django* (Oct 11-15, 2026).

<!-- TODO [Day 5 · P3]: Complete every section marked "TODO" on Day 5, after your deployment works.
     Test it: a classmate must be able to clone, set up, test, and use your API from this README alone.
     HINT: days/day-05/hints.md#p3 -->

**Live API:** _TODO: https://<your-app>.onrender.com_

## Tech stack

Python 3.13 · Django 5.2 · Django REST Framework 3.16 (token auth) · SQLite (local) · PostgreSQL on Neon (production) · Render

## Local setup

```bash
git clone https://github.com/<your-username>/task-management-api.git
cd task-management-api

# Windows PowerShell                     # macOS Terminal
py -m venv .venv                         # python3 -m venv .venv
.venv\Scripts\Activate.ps1               # source .venv/bin/activate

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Environment variables

_TODO: list every variable from `.env.example`, what it does, and its local default._

## Create test users

_TODO: explain how a reviewer creates users to try the API (admin or command)._

## Run the tests

_TODO: the test command and what a passing run looks like._

## Authentication

_TODO: how to obtain a token and how to send it with each request._

## Endpoints

| Method | Path | Purpose | Success |
|---|---|---|---|
| POST | `/api/auth/token/` | Exchange username/password for a token | 200 |
| GET | `/api/tasks/` | List **your** tasks (newest first) | 200 |
| POST | `/api/tasks/` | Create a task owned by you | 201 |
| GET | `/api/tasks/{id}/` | Retrieve one of your tasks | 200 |
| PUT / PATCH | `/api/tasks/{id}/` | Replace / partially update one of your tasks | 200 |
| DELETE | `/api/tasks/{id}/` | Delete one of your tasks | 204 |

### Example: create a task

```http
POST /api/tasks/
Authorization: Token <token>
Content-Type: application/json

{"title": "Prepare demo", "description": "Day 5 live demo", "status": "TODO", "due_date": "2026-10-15"}
```

Response `201 Created`:

```json
{
  "id": 7,
  "title": "Prepare demo",
  "description": "Day 5 live demo",
  "status": "TODO",
  "due_date": "2026-10-15",
  "owner": "alice",
  "created_at": "2026-10-14T10:02:11.512301+03:00",
  "updated_at": "2026-10-14T10:02:11.512301+03:00"
}
```

_TODO: add examples for update (PATCH), a validation error (400), and another user's task (404)._

### Field rules

| Field | Rules |
|---|---|
| `title` | required, not blank, max 200 characters |
| `description` | optional |
| `status` | `TODO` (default), `IN_PROGRESS`, or `DONE` |
| `due_date` | optional `YYYY-MM-DD`; cannot be earlier than today when a task is created |
| `id`, `owner`, `created_at`, `updated_at` | read-only, set by the server |

## Deployment

_TODO: document the platform, build/start commands, environment variables, and how you verified the release._

## Project decisions

_TODO: 3-5 bullet points explaining important choices you made and why._
