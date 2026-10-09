# Task Management API

A personal task management REST API built with Django and Django REST Framework during the
Tuwaiq Club at KFUPM bootcamp *Building REST APIs with Django* (Oct 25-29, 2026).

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
