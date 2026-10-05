# Deployment Runbook: Render + Neon (Day 5)

Deploy your Task Management API as a **public HTTPS** service with a **persistent PostgreSQL** database, for free.
Rehearse steps 1-2 on Day 4 and run the whole sequence on Day 5.

```text
1. code ready → 2. Neon database → 3. Render web service → 4. environment variables → 5. build + start
→ 6. production users → 7. smoke test → 8. persistence check
```

Write down each gate's result (URL or command output) as evidence. **Never** record secret values.

## 1. Code ready (local)

Your repository on GitHub contains (Day 4 + Day 5 TODOs):

- [ ] `requirements.txt` with Django, DRF, `psycopg[binary]`, `dj-database-url`, `gunicorn`, `whitenoise`
- [ ] `.python-version` containing `3.13`
- [ ] settings: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` from the environment; `DATABASE_URL`
  switch; WhiteNoise; `STATIC_ROOT`
- [ ] `python manage.py test` passes and `python manage.py collectstatic --noinput` succeeds
- [ ] `.env` and `db.sqlite3` are **not** in Git (`git status` is clean after `git add .`)

## 2. Neon database

1. https://neon.com → **New project** → name `tuwaiq-django-api` → choose the region closest to your Render
   region → create.
2. **Connect** → copy the connection string. It looks like
   `postgresql://USER:PASSWORD@ep-xxxx.REGION.aws.neon.tech/neondb?sslmode=require`.
3. Keep it in your clipboard or a password manager. **Do not** paste it into any file, commit, or chat.

## 3. Render web service

1. https://dashboard.render.com → **New → Web Service** → select your `task-management-api` repository.
2. Settings:

   | Setting | Value |
   |---|---|
   | Name | e.g. `task-api-yourname` (it becomes `task-api-yourname.onrender.com`) |
   | Language / Runtime | **Python** |
   | Branch | `main` |
   | Build command | `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate` |
   | Start command | `gunicorn config.wsgi:application` |
   | Instance type | **Free** |

## 4. Environment variables (Render → Environment)

| Key | Value |
|---|---|
| `DATABASE_URL` | the Neon connection string (secret) |
| `SECRET_KEY` | a long random value: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `task-api-yourname.onrender.com` |
| `CSRF_TRUSTED_ORIGINS` | `https://task-api-yourname.onrender.com` |

## 5. Build and start

Click **Create Web Service** (or **Manual Deploy**). Watch the **Logs**:

- the build installs the packages, collects static files, and runs `Applying tasks.0001_initial... OK`
- the start shows `Listening at: http://0.0.0.0:10000` (or similar) and `Your service is live`

Open `https://<app>.onrender.com/api/tasks/`. Expected: `401` with
`{"detail": "Authentication credentials were not provided."}`. That proves the API is live and protected.

Failure? Read the **first** error in the log and use
[`troubleshooting.md`](troubleshooting.md#deployment-problems-render--neon).

## 6. Create users in production

The Neon database starts **empty**. Your local users do not exist there.

- **Option A: Render Shell** (if your plan offers the Shell tab): `python manage.py createsuperuser`
- **Option B: from your laptop**, in a **new** terminal inside your project with `.venv` active:

  ```powershell
  $env:DATABASE_URL = "<paste the Neon string here, in the terminal only>"     # macOS: export DATABASE_URL="..."
  python manage.py createsuperuser
  ```

  Then **close that terminal**, so you cannot accidentally run local commands against production.

Then open `https://<app>.onrender.com/admin/`, log in, and add two normal users (e.g. `alice`, `bob`).

## 7. Smoke test

```bash
python smoke_test.py --base-url https://<app>.onrender.com --user alice --other-user bob
```

Expected: `10/10 checks passed`. Copy the output (it contains no tokens) into your evidence.

## 8. Persistence check

1. With Postman (`Render` environment), create a task named `Persistence check`.
2. Render → **Manual Deploy → Restart service** (or push a small README change to trigger a redeploy).
3. `GET /api/tasks/`: `Persistence check` is still there.

## Free-plan behaviour

- Free Render services **sleep after ~15 minutes** without traffic. The first request can take up to a minute, so open
  the URL before your demo.
- The Render server's disk is **not persistent**. That is why the data lives in Neon PostgreSQL, not SQLite.
- Free-plan limits can change. Check https://render.com/docs/free and Neon's pricing page if something looks
  different from this guide.
