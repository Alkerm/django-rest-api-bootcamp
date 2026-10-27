# Project checkpoints

Each folder is a **complete, runnable** Task Management API at the **start** of a day:
every previous day is already solved, and that day's work is marked with `TODO [Day N · Pn]` comments.

| Folder | Contains (solved) | Today's TODOs |
|---|---|---|
| [`../starter/`](../starter/) | generated Django project | Day 1: apps, `Task` model, `__str__`, admin |
| [`day-02/`](day-02/) | Day 1 | Day 2: ordering, `task_to_dict`, five function views, `path()` URLs |
| [`day-03/`](day-03/) | Days 1-2 | Day 3: `TaskSerializer`, serializer in every view, validation (+ stretch: owner as username) |
| [`day-04/`](day-04/) **(final)** | Days 1-3 | **Day 4 + Day 5**: token auth, owner filter + `get_own_task`, env settings, `.env.example` · then the README; `smoke_test.py` included |

**Released one day at a time.** Each checkpoint contains the solved work of the previous days, so it is published
in this repository on the **morning of the day it is for** (e.g. `day-03/` appears on Day 3). Until then the folder
holds only a short note. When the instructor announces it, run `git -C django-rest-api-bootcamp pull`.

## Using a checkpoint

**Days 2-4: everyone copies the whole checkpoint at the start of the day** (exact commands on each day's
`project-milestone.md`). Keep your own `.git` and `.venv`; your database is not part of a checkpoint, so your users
and tasks stay as they are. Then run `python manage.py migrate`.

**`day-04` is the last copy.** It already contains the Day 5 TODOs, so on Day 5 you keep working in the same project
and copy nothing.

The migration files have exactly the names Django generates for you (`0001_initial.py`, `0002_alter_task_options.py`),
so a checkpoint copy simply replaces your own copy of the same migration.
