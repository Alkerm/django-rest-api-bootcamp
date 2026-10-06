# Day 5 Hints

Open the hints **one level at a time**. Level 3 is close to the answer.

**Exercise:** [Task 1](#task-1) · [Task 2](#task-2) · [Task 3](#task-3)
**Project:** [P1](#p1) · [P2](#p2) · [P3](#p3) · [Deployment problems](#deploy)

---

## Exercise

<a id="task-1"></a>
### Task 1: `DATABASE_URL`

<details><summary>Level 1: nudge</summary>

Keep the SQLite `DATABASES` as it is. **Below** it, add an `if` that replaces `DATABASES` only when the variable
exists. See [`example/settings_production.py`](example/settings_production.py).
</details>

<details><summary>Level 2: almost the answer</summary>

```python
if os.getenv("DATABASE_URL"):
    DATABASES = {
        "default": dj_database_url.config(conn_max_age=600, conn_health_checks=True),
    }
```
</details>

<details><summary>How do I know which database Django uses?</summary>

```bash
python manage.py shell -c "from django.db import connection; print(connection.vendor, connection.settings_dict['NAME'])"
```
</details>

<a id="task-2"></a>
### Task 2: Static files

<details><summary>Level 1: nudge</summary>

Two edits: one line in `MIDDLEWARE` (directly after `SecurityMiddleware`), and two settings below `STATIC_URL`.
</details>

<details><summary>Common errors</summary>

| Symptom | Cause |
|---|---|
| `ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting` | `STATIC_ROOT` missing |
| Admin page without styling while `DEBUG=False` | WhiteNoise middleware missing, or `collectstatic` not run |
| `ValueError: Missing staticfiles manifest entry` | you used `CompressedManifestStaticFilesStorage`: use `CompressedStaticFilesStorage` as in the TODO |
| `Bad Request (400)` in the browser | `ALLOWED_HOSTS` does not contain `127.0.0.1` (check your environment variables) |
</details>

<a id="task-3"></a>
### Task 3: The smoke test

<details><summary>Level 1: nudge</summary>

`list_requires_auth()` is a complete example of one request. Every function you write follows the same 2 steps:
send the request with `requests.<method>(...)` and return what the docstring asks for.
See [`example/smoke_example.py`](example/smoke_example.py).
</details>

<details><summary>Level 2: almost the answer</summary>

```python
def get_token(base_url, username, password):
    response = requests.post(f"{base_url}/api/auth/token/",
                             json={"username": username, "password": password}, timeout=TIMEOUT)
    if response.status_code == 200:
        return response.json()["token"]
    return None

def get_item_status(base_url, token, item_id):
    response = requests.get(f"{base_url}/api/reading-list/{item_id}/", headers=auth_headers(token), timeout=TIMEOUT)
    return response.___
```
</details>

<details><summary><code>requests.exceptions.ConnectionError</code></summary>

The server is not running (or runs on another port). Start it in a different terminal first.
</details>

---

## Project

<a id="p1"></a>
### P1: `DATABASE_URL`

<details><summary>Level 1</summary>

Keep the SQLite `DATABASES` as it is and add an `if os.getenv("DATABASE_URL"):` block below it (see
[`example/settings_production.py`](example/settings_production.py)). Locally nothing changes; on Render, `DATABASE_URL`
holds your Neon connection string. WhiteNoise, static files and CSRF origins are already written for you.
</details>

<a id="p2"></a>
### P2: `.env.example`

<details><summary>Level 1</summary>

```text
DATABASE_URL=postgresql://USER:PASSWORD@HOST/DBNAME?sslmode=require
CSRF_TRUSTED_ORIGINS=https://your-app-name.onrender.com
```
Placeholders only. **Never** paste your real Neon string here.
</details>

<a id="p3"></a>
### P3: Final README

<details><summary>Level 1: what goes in</summary>

Fill **every** `_TODO_` section of the README that arrived with the Day 4 checkpoint, plus the two Day 5 parts: your
real `https://...onrender.com` URL at the top, and a **Deployment** section (platform, build command, start command,
environment variable *names* only, and your smoke-test result).
</details>

<details><summary>Level 2: who it is for</summary>

Write for a classmate who has never seen your project. Each `_TODO_` section needs real commands or examples that
**work when copied**. The test: swap repositories with a partner, follow only the README, and note every place where
they got stuck.
</details>

<details><summary>Level 3: checklist from the program brief</summary>

The README must cover: setup, environment variables, migrations, test command, authentication, endpoint examples,
deployed URL (Day 5), and project decisions.
</details>

<a id="deploy"></a>
### Deployment problems

<details><summary>Where to look first</summary>

Render → your service → **Logs**. Read the **first** error, not the last. Then use the table in
[`example/README.md`](example/README.md#reading-deploy-logs-where-does-it-fail) or
[`setup/troubleshooting.md`](../../setup/troubleshooting.md).
</details>

<details><summary>The deploy succeeded but <code>/api/auth/token/</code> says the credentials are wrong</summary>

The production database is **new and empty**: your local users are not there. Create users against production:
Render **Shell** tab → `python manage.py createsuperuser`, then add users in `https://<app>.onrender.com/admin/`.
(No Shell on the free plan? Run `python manage.py createsuperuser` locally in a terminal where `DATABASE_URL` is set to
the Neon string, then close that terminal.)
</details>

<details><summary>The first request takes ~50 seconds</summary>

Free Render services sleep after 15 minutes without traffic. Open the URL a minute before your demo.
</details>
