# Task Management API

A personal task management REST API built with **Django 5.2** and **Django REST Framework 3.16**.
Each authenticated user creates and manages **only their own tasks**: the API validates input, protects every task
endpoint with token authentication, and blocks access to other users' data.

Built during the Tuwaiq Club at KFUPM bootcamp *Building REST APIs with Django* (Oct 11-15, 2026).

<!-- TODO [Day 5 · P6]: Fill in the live URL and the Deployment section after your release succeeds.
     HINT: days/day-05/hints.md#p6 -->

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

Locally **no variables are required**: the defaults are safe for development. Production values are set on Render
(see [`.env.example`](.env.example)). Never commit real values.

| Variable | Purpose | Local default | Production |
|---|---|---|---|
| `SECRET_KEY` | Django cryptographic signing | `development-only-key` | long random value (secret) |
| `DEBUG` | Debug pages and error details | `True` | `False` |
| `ALLOWED_HOSTS` | Host names the app may serve | `127.0.0.1,localhost` | `<app>.onrender.com` |

## Create test users

```bash
python manage.py createsuperuser          # admin account for http://127.0.0.1:8000/admin/
```

Create at least two normal users (for example `alice` and `bob`) in the admin under **Users -> Add user**,
or from the shell:

```bash
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('alice', password='choose-a-password')"
```

## Run the tests

```bash
python manage.py test
```

Expected: `Ran 15 tests ... OK`. The tests create their own users and tasks in a temporary database: they cover
authentication, CRUD, ownership/data isolation, and validation.

## Authentication

1. Exchange a username and password for a token:

   ```http
   POST /api/auth/token/
   Content-Type: application/json

   {"username": "alice", "password": "<password>"}
   ```

   Response `200 OK`: `{"token": "<40-character token>"}`

2. Send the token with every task request:

   ```http
   Authorization: Token <40-character token>
   ```

Requests without a valid token receive `401 Unauthorized`.

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

### Example: partial update

```http
PATCH /api/tasks/7/
Authorization: Token <token>
Content-Type: application/json

{"status": "DONE"}
```

Response `200 OK` with the full task, `"status": "DONE"`.

### Example: validation error

```http
POST /api/tasks/
Authorization: Token <token>
Content-Type: application/json

{"title": "  ", "status": "FINISHED", "due_date": "2020-01-01"}
```

Response `400 Bad Request`:

```json
{
  "title": ["Title cannot be blank."],
  "status": ["\"FINISHED\" is not a valid choice."],
  "due_date": ["Due date cannot be earlier than today."]
}
```

### Example: another user's task

`GET /api/tasks/{id-of-bobs-task}/` with Alice's token returns `404 Not Found`: other users' tasks are invisible.

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

- **Token authentication (DRF `authtoken`)**: simple to use from Postman and tests; JWT was out of scope.
- **Other users' tasks return 404, not 403**: the queryset only contains the caller's tasks, so the API does not
  even reveal that another user's task id exists.
- **Owner is read-only and set from the token**: a client can never create or move a task into another account.
- **Due date is checked only on create** (Riyadh local date): an existing task may become overdue and still be edited.
- **SQLite locally, PostgreSQL in production**: zero local setup, persistent managed storage on Neon.
