# Day 5 Worked Example: From Laptop to Production

| File | Shows |
|---|---|
| [`settings_production.py`](settings_production.py) | `DATABASE_URL` with `dj-database-url`, WhiteNoise, `STATIC_ROOT`, `CSRF_TRUSTED_ORIGINS`, HTTPS settings behind a proxy |
| [`smoke_example.py`](smoke_example.py) | sending real HTTP requests with `requests` |

## Same code, different configuration

| | Laptop | Render (production) |
|---|---|---|
| Server | `python manage.py runserver` | `gunicorn config.wsgi:application` |
| Database | SQLite file `db.sqlite3` | PostgreSQL on Neon (`DATABASE_URL`) |
| `DEBUG` | `True` (default) | `False` |
| `SECRET_KEY` | development default | long random secret |
| Static files | served by `runserver` | collected by `collectstatic`, served by WhiteNoise |
| Disk | permanent | **temporary**: files written at runtime disappear on restart, so data must live in PostgreSQL |

## The release sequence

```text
1. connect GitHub repo → 2. create database (Neon) → 3. set environment variables
→ 4. build (pip install, collectstatic, migrate) → 5. start (gunicorn) → 6. verify (smoke test)
```

## Reading deploy logs: where does it fail?

| Log symptom | Category | Typical fix |
|---|---|---|
| `ERROR: Could not find a version that satisfies ...` | dependency install | fix the package name/version in `requirements.txt` |
| `ModuleNotFoundError: No module named 'whitenoise'` | dependency missing | add the package to `requirements.txt`, push again |
| `ImproperlyConfigured: Set the SECRET_KEY ...` | configuration | add `SECRET_KEY` in Render → Environment |
| `DisallowedHost: Invalid HTTP_HOST header` / browser shows *Bad Request (400)* | host settings | add `<app>.onrender.com` to `ALLOWED_HOSTS` |
| `could not translate host name` / `password authentication failed` | database connectivity | copy a fresh Neon connection string into `DATABASE_URL` (keep `?sslmode=require`) |
| `relation "tasks_task" does not exist` | migrations not run | make sure the build command ends with `python manage.py migrate` |
| `CSRF verification failed` on the admin login | CSRF origin | set `CSRF_TRUSTED_ORIGINS=https://<app>.onrender.com` |

Read the **first** meaningful error in the log. Later lines are usually consequences of it.
