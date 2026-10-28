# Day 1 Worked Example: Movies

A short, **read-only** example of today's concepts in a different domain (movies). It is not a project you run.
Open these files next to the exercise or project when you are unsure about the syntax.

| File | Shows |
|---|---|
| [`models.py`](models.py) | `CharField`, `TextField`, `DateField`, choices with `TextChoices`, `unique=True`, `ForeignKey` (to a model and to the user model), `auto_now_add` / `auto_now`, `Meta.ordering`, `__str__` |
| [`admin.py`](admin.py) | `admin.site.register` and a customised `ModelAdmin` (`list_display`, `list_filter`, `search_fields`) |
| [`orm_examples.py`](orm_examples.py) | Create, read (`filter`, lookups like `__gt`, following a ForeignKey with `__`), update, delete |

## Client and server

```text
 CLIENT (browser, Postman, mobile app)                         SERVER (your Django project)
   sends a REQUEST  ───────────── HTTP over the network ─────────────▶  reads it, does the work, talks to the database
   receives the RESPONSE  ◀──────────────────────────────────────────  answers with a status code + data (JSON)
```

The client never touches the database: it can only send requests. The server decides what is allowed.

## Anatomy of an HTTP request and response

```http
POST /api/tasks/create/ HTTP/1.1          ← method (the action) + path (the resource) + protocol
Host: 127.0.0.1:8000                      ← headers: extra information about the request
Content-Type: application/json            ←   "the body is JSON"
Authorization: Token 9944b09199c6...      ←   who is asking (Day 4)
                                          ← an empty line separates headers from the body
{"title": "Prepare slides", "status": "TODO"}     ← body: the data sent (POST, PUT, PATCH)
```

```http
HTTP/1.1 201 Created                      ← status code: did it work? 2xx yes, 4xx client error, 5xx server error
Content-Type: application/json

{"id": 7, "title": "Prepare slides", "status": "TODO", "owner": "alice", ...}
```

| Status | Meaning | Status | Meaning |
|---|---|---|---|
| `200 OK` | read / changed | `401 Unauthorized` | who are you? (no or bad token) |
| `201 Created` | a new row exists | `403 Forbidden` | known, but not allowed |
| `204 No Content` | deleted, empty body | `404 Not Found` | no such resource (for you) |
| `400 Bad Request` | invalid input | `405 Method Not Allowed` | this URL does not accept that method |

## What is a web framework?

Every web application has to do the same jobs again and again: match a URL to code (**routing**), parse requests,
talk to a database, build responses, check who the user is, and protect against common attacks. A **framework** is
code that already does these jobs, so you only write what is special about *your* application.

| Job | Without a framework | With Django + DRF |
|---|---|---|
| URL → code | parse the path yourself | `path("tasks/", views.list_tasks)` (Day 2) |
| Database | write SQL by hand | models + the ORM: `Task.objects.filter(...)` |
| Tables | `CREATE TABLE ...` by hand | `makemigrations` + `migrate` |
| JSON in/out | `json.loads` / `json.dumps` everywhere | `request.data`, `Response(...)` (Day 2), serializers (Day 3) |
| Admin UI | build it yourself | `admin.site.register(Task)` |
| Login, tokens | build it yourself | `django.contrib.auth`, DRF tokens (Day 4) |

Django is the web framework; **Django REST Framework (DRF)** is an add-on for building APIs that speak JSON.

## Databases 101

A relational database stores data in **tables**. A table is like a spreadsheet with strict rules:

**Table `movies_director`**

| id (PK) | name | birth_year |
|---|---|---|
| 1 | Christopher Nolan | 1970 |
| 2 | Greta Gerwig | 1983 |

**Table `movies_movie`**

| id (PK) | title | genre | imdb_code (unique) | director_id (FK → movies_director.id) |
|---|---|---|---|---|
| 1 | Inception | DRAMA | tt1375666 | 1 |
| 2 | Oppenheimer | DRAMA | tt15398776 | 1 |
| 3 | Lady Bird | COMEDY | tt4925292 | 2 |

| Word | Meaning | In Django |
|---|---|---|
| **table** | one kind of thing | one model class (`Movie`) |
| **column** | one property, with a type | one field (`title = models.CharField(...)`) |
| **row** | one thing | one object (`Movie(title="Inception")`) |
| **primary key (PK)** | the unique id of a row, never reused | `id`, added automatically |
| **foreign key (FK)** | a column that stores another table's id: a relationship | `models.ForeignKey(Director, ...)` → column `director_id` |
| **constraint** | a rule the database enforces (`NOT NULL`, `UNIQUE`) | `unique=True`, a field without `null=True` |

"Many movies belong to one director" is stored as `director_id` on **each movie**, not as a list on the director.

### SQL vs the ORM

The database only understands **SQL**. The Django **ORM** writes the SQL for you:

| ORM (Python) | SQL that Django sends (simplified) |
|---|---|
| `Movie.objects.all()` | `SELECT * FROM movies_movie;` |
| `Movie.objects.filter(genre="DRAMA")` | `SELECT * FROM movies_movie WHERE genre = 'DRAMA';` |
| `Movie.objects.filter(director__name="Greta Gerwig")` | `SELECT movies_movie.* FROM movies_movie JOIN movies_director ON movies_movie.director_id = movies_director.id WHERE movies_director.name = 'Greta Gerwig';` |
| `Movie.objects.create(title="Dune", ...)` | `INSERT INTO movies_movie (title, ...) VALUES ('Dune', ...);` |
| `movie.delete()` | `DELETE FROM movies_movie WHERE id = 3;` |

See the SQL of any query in the shell: `print(Movie.objects.filter(genre="DRAMA").query)`.

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
