# Day 1 Worked Example: Movies

A short, **read-only** example of today's concepts in a different domain (movies). It is not a project you run.
Open these files next to the exercise or project when you are unsure about the syntax.

| File | Shows |
|---|---|
| [`models.py`](models.py) | `CharField`, `TextField`, `DateField`, choices with `TextChoices`, `unique=True`, `ForeignKey` (to a model and to the user model), `auto_now_add` / `auto_now`, `Meta.ordering`, `__str__` |
| [`admin.py`](admin.py) | `admin.site.register` and a customised `ModelAdmin` (`list_display`, `list_filter`, `search_fields`) |
| [`orm_examples.py`](orm_examples.py) | Create, read (`filter`, lookups like `__gt`, following a ForeignKey with `__`), update, delete |

## The model → migration → database flow

```text
models.py  --(python manage.py makemigrations)-->  migrations/0001_initial.py  --(python manage.py migrate)-->  db.sqlite3 tables
  Python class                                       a recipe of changes                                      real rows and columns
```

- Change a model → run **both** commands again. `makemigrations` writes a *new* numbered file and never edits old ones.
- `python manage.py showmigrations` lists which migrations are applied (`[X]`).
- Migrations are **committed to Git**, so every developer and the production server build the same tables.
  The `db.sqlite3` file is **not** committed: anyone can rebuild it with `migrate`.

## Field options you will use most

| Option | Meaning |
|---|---|
| `max_length=200` | required for `CharField` |
| `blank=True` | the field may be left empty in forms/validation |
| `null=True` | the database column may store NULL (use it for dates/numbers that can be "unknown", not for text) |
| `default=...` | value used when none is given |
| `unique=True` | no two rows may have the same value |
| `choices=...` | only listed values are valid |
| `on_delete=models.CASCADE` | deleting the parent deletes its children |
| `related_name="movies"` | name of the reverse relationship: `director.movies.all()` |
