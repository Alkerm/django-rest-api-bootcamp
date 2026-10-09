# Troubleshooting

Use the **exact** error message when asking for help. Do not reinstall everything before you know which component
fails.

## Setup problems

| Problem | Likely cause | Action |
|---|---|---|
| `python` / `py` not found | PATH/launcher missing, or terminal opened before install | restart the terminal/computer; re-run the Python installer with PATH/launcher enabled |
| Wrong Python in VS Code | system interpreter selected instead of `.venv` | **Python: Select Interpreter** → choose `.venv` |
| `Activate.ps1 cannot be loaded because running scripts is disabled` | PowerShell execution policy | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then reopen the terminal |
| `ModuleNotFoundError: No module named 'django'` / pip installs globally | virtual environment not active | activate `.venv`; the prompt must show `(.venv)` |
| `Error: That port is already in use` | another server is still running | stop it (Ctrl+C in its terminal) or `python manage.py runserver 8001` |
| `database is locked` | DB Browser and Django write at the same time | close DB Browser or revert its unsaved edits |
| `git push` rejected / asks for a password | authentication or remote URL issue | sign in through VS Code or the browser prompt; check `git remote -v` |
| `warning: ... LF will be replaced by CRLF` (or `CRLF ... by LF`) | Windows line-ending notice from Git | harmless, nothing to fix; the project's `.gitattributes` keeps line endings consistent |
| `ssl.SSLCertVerificationError` / `CERTIFICATE_VERIFY_FAILED` (macOS), e.g. in `smoke_test.py` | the python.org installer's certificates were never installed | run `open "/Applications/Python 3.13/Install Certificates.command"`, then retry (see [installation](installation.md)) |
| `git pull` of the bootcamp repo: *Your local changes ... would be overwritten* | you edited exercise files that the instructor also updated | `git -C django-rest-api-bootcamp stash`, then `pull`, then `git -C django-rest-api-bootcamp stash pop` |

## Django and DRF errors

| Error / symptom | Meaning | Fix |
|---|---|---|
| `No changes detected` | the model file was not saved, or the app is not in `INSTALLED_APPS` | save; check `INSTALLED_APPS` |
| `no such table: ...` | migrations not applied | `python manage.py migrate` |
| `You are trying to add a non-nullable field ...` | a required field was added to a table that already has rows | add a `default`, or (exercise only) delete `db.sqlite3` + the new migration and repeat |
| `NOT NULL constraint failed: tasks_task.<field>` (e.g. `due_date`) right after copying a checkpoint | your Day 1 model differed from the field table, so your database was built from a different migration than the checkpoint's | delete `db.sqlite3`, run `python manage.py migrate`, recreate your users with `createsuperuser` + the admin (2 minutes) |
| `NOT NULL constraint failed: tasks_task.owner_id` | the owner is not set on create | `perform_create` → `serializer.save(owner=self.request.user)` |
| `RuntimeError: Model class rest_framework.authtoken.models.Token doesn't declare an explicit app_label` | `obtain_auth_token` imported before `rest_framework.authtoken` is installed | add `rest_framework.authtoken` to `INSTALLED_APPS`, then `migrate` |
| `ImproperlyConfigured: Field name 'x' is not valid for model ...` | a name in `fields` is not a model field and is not declared on the serializer | fix the spelling, or declare the extra field |
| `DisallowedHost` / browser shows *Bad Request (400)* | host not in `ALLOWED_HOSTS` | check the `ALLOWED_HOSTS` environment variable |

## API client (Postman) problems

| Response | Likely cause | Fix |
|---|---|---|
| `401 Authentication credentials were not provided.` | no `Authorization` header | add `Authorization: Token {{token}}` |
| `401 Invalid token.` | expired/wrong token or wrong prefix | get a new token; the header is `Token <key>` (word, space, key) |
| `403 Authentication credentials were not provided.` | `SessionAuthentication` is listed before `TokenAuthentication` | put `TokenAuthentication` first |
| `404 Not Found` | wrong URL, missing trailing slash, wrong id, or the object belongs to another user | check `base_url`, the route, the trailing `/`, the id, and which user's token you use |
| `405 Method Not Allowed` | the method is not allowed on that URL (e.g. `PUT` on the list URL) | use the detail URL `/api/tasks/{id}/` |
| `415 Unsupported Media Type` | body not sent as JSON | Body → **raw** → **JSON** |

## Deployment problems (Render + Neon)

| Symptom | Likely cause | Action |
|---|---|---|
| build fails | build command, dependency, or Python version | read the **first** error in the build log; check `requirements.txt` |
| `ModuleNotFoundError` at start | package missing from `requirements.txt` | add it, commit, push |
| `ImproperlyConfigured: Set the SECRET_KEY ...` | variable missing | add `SECRET_KEY` in Render → Environment |
| *Bad Request (400)* | `ALLOWED_HOSTS` does not include the Render hostname | `ALLOWED_HOSTS=<app>.onrender.com` |
| Neon connection fails | incorrect/expired URL or a space in the value | copy a fresh connection string, keep `?sslmode=require` |
| `relation "tasks_task" does not exist` | migrations did not run | the build command must end with `python manage.py migrate` |
| Admin login → *CSRF verification failed* | origin not trusted | `CSRF_TRUSTED_ORIGINS=https://<app>.onrender.com` |
| Token login fails in production | production database has no users | create users in production (see [`deployment.md`](deployment.md#6-create-users-in-production)) |
| First request takes ~1 minute | free service was asleep | open the URL before the demo |

## A good support request

Include: operating system and version · the exact command · the **complete** error text · what you expected · what
changed just before the error · the output of the relevant version command. **Remove passwords, tokens, and secrets
first.**

## Recovery plan when local setup fails

Use the first option that works:

1. Copy the exact error, use the tables above, retry **only** the failed step, and repeat the readiness check.
2. Attend the **setup clinic** at least 48 hours before Day 1 with the same laptop, charger, administrator access,
   and account access.
3. Use a **club-prepared backup laptop** with the approved versions and a fresh participant profile.
4. If no backup laptop is available, the Technical Lead may assign an instructor-prepared browser-based workspace
   (tested with this project before it is offered).
5. After recovery, repeat the readiness check and submit the same evidence as everyone else.

A recovery environment is temporary: you still need your own GitHub repository and must understand every command.
