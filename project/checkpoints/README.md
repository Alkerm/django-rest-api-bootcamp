# Project checkpoints

Each folder is a **complete, runnable** Task Management API at the **start** of a day:
every previous day is already solved, and that day's work is marked with `TODO [Day N · Pn]` comments.

| Folder | Contains (solved) | Today's TODOs |
|---|---|---|
| [`../starter/`](../starter/) | generated Django project | Day 1: apps, `Task` model, `__str__`, admin |
| [`day-02/`](day-02/) | Day 1 | Day 2: ordering, serializer, viewset, router, URLs |
| [`day-03/`](day-03/) | Days 1-2 | Day 3: token auth, `get_queryset`, `IsOwner`, validation |
| [`day-04/`](day-04/) | Days 1-3 | Day 4: tests, env settings, `.env.example`, requirements, README |
| [`day-05/`](day-05/) | Days 1-4 | Day 5: `DATABASE_URL`, WhiteNoise, static files, CSRF origins, README |

## Using a checkpoint

**On track:** keep working in your own repository and copy only the **new** files the day's
`project-milestone.md` lists, then add the TODO code where the comments show.

**Behind:** copy the whole checkpoint over your project folder. Keep your own `.git` (your history) and `.venv`
folders. Then:

```bash
python -m pip install -r requirements.txt
python manage.py migrate
git add . && git commit -m "Start Day N from checkpoint" && git push
```

Your database (`db.sqlite3`) is not part of a checkpoint, so your users and tasks stay as they are.
