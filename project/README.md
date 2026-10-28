# Task Management API

A personal task management REST API built with **Django 5.2** and **Django REST Framework 3.16** during the
Tuwaiq Club at KFUPM bootcamp *Building REST APIs with Django* (October 2026).

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

1. Log in through the browsable API: http://127.0.0.1:8000/api-auth/login/
2. Open http://127.0.0.1:8000/api/tasks/

| Method | Path | Purpose | Success |
|---|---|---|---|
| GET | `/api/tasks/` | List tasks (newest first) | 200 |
| POST | `/api/tasks/create/` | Create a task (the owner is set by the server) | 201 |
| GET | `/api/tasks/{id}/` | Retrieve one task | 200 |
| PUT / PATCH | `/api/tasks/{id}/update/` | Replace / partially update a task | 200 |
| DELETE | `/api/tasks/{id}/delete/` | Delete a task | 204 |

Invalid input returns `400` with field errors, for example `{"title": ["Title cannot be blank."]}`.
