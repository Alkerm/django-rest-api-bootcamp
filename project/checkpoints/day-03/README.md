# Task Management API

A personal task management REST API built with Django and Django REST Framework during the
Tuwaiq Club at KFUPM bootcamp *Building REST APIs with Django* (Oct 11-15, 2026).

> This README grows during the week. On Day 4 you will replace it with the full project README
> (setup, environment variables, tests, authentication, endpoint examples, deployment).

## Run locally

```bash
# Windows PowerShell                     # macOS Terminal
py -m venv .venv                         # python3 -m venv .venv
.venv\Scripts\Activate.ps1               # source .venv/bin/activate

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/admin/ and sign in with the superuser you created.

## API

Get a token, then send it with every request:

```http
POST /api/auth/token/
Content-Type: application/json

{"username": "alice", "password": "<password>"}
```

Response: `{"token": "<40-character token>"}`. Header for every task request: `Authorization: Token <token>`.
Requests without a token get `401`; other users' tasks return `404`.

| Method | Path | Purpose |
|---|---|---|
| POST | `/api/auth/token/` | Exchange username + password for a token |
| GET | `/api/tasks/` | List **your** tasks |
| POST | `/api/tasks/` | Create a task (owner is set by the server) |
| GET | `/api/tasks/{id}/` | Retrieve one of your tasks |
| PUT / PATCH | `/api/tasks/{id}/` | Replace / partially update one of your tasks |
| DELETE | `/api/tasks/{id}/` | Delete one of your tasks |
