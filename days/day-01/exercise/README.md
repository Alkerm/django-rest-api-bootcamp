# Day 1 Exercise: Library Catalog (Models, Migrations, Admin, ORM)

| | |
|---|---|
| **What you will practice** | Defining a Django model with a relationship · creating and applying migrations · loading sample data · registering models in the admin · reading and writing data with the ORM |
| **Where to start** | This folder: `days/day-01/exercise/`. Files: `catalog/models.py` → `catalog/admin.py` → `orm_practice.py` |
| **Result to produce** | **Core:** a migrated SQLite database with 3 authors and 6 books, a working admin for both models, and ORM functions 1-3 passing. **Stretch:** functions 4-5 (`Stretch: 2/2 passed`) |
| **Time** | ~45 minutes |
| **Hints** | [`../hints.md`](../hints.md) · worked example: [`../example/`](../example/) |

---

## Before you start

Run these in a terminal **opened in this folder** (`days/day-01/exercise`):

```bash
# 1. Activate the bootcamp virtual environment (created once at the repository root - see setup/installation.md)
..\..\..\.venv\Scripts\Activate.ps1          # Windows PowerShell
source ../../../.venv/bin/activate            # macOS

# 2. Confirm Django can load the project
python manage.py check                        # -> System check identified no issues (0 silenced).
```

> **Database state at the start: there is NO database yet.** `db.sqlite3` does not exist and there is no data.
> You create the tables in Task 2 and load the sample data at the end of Task 2.
> Do **not** run `migrate` before finishing Task 1; otherwise you need an extra migration later.

This exercise uses its **own** database file: `days/day-01/exercise/db.sqlite3`. It is ignored by Git and you can
delete it at any time and rebuild it with Task 2's commands.

---

## Task 1: Complete the `Book` model

**File:** `catalog/models.py`. Find `TODO [Day 1 · Task 1]`.

`Author` is already written. Use it as your pattern. Complete `Book` so it matches this structure:

**Table `catalog_book`** (one row = one book)

| Field | Django type | Rules | Example value |
|---|---|---|---|
| `id` | BigAutoField | automatic primary key, **do not add it** | `1` |
| `title` | `CharField` | `max_length=200` | `"Clean Code"` |
| `isbn` | `CharField` | `max_length=13`, `unique=True` | `"9780000000011"` |
| `published_year` | `PositiveIntegerField` | required | `2008` |
| `available_copies` | `PositiveIntegerField` | `default=1` | `3` |
| `author` | `ForeignKey → Author` | **given**: `on_delete=CASCADE`, `related_name="books"` | `1` (stored as `author_id`) |

**Relationship:** one `Author` → many `Book`s. From a book: `book.author.name`. From an author: `author.books.all()`.

Also complete `__str__` so a book displays as its title.

**Acceptance criteria**
- [ ] `python manage.py check` prints *no issues*.
- [ ] All four fields exist with exactly the names above (the sample data in Task 2 uses these names).

---

## Task 2: Create the database and load sample data

**No code to write: run the commands and read their output.**

```bash
python manage.py makemigrations catalog    # turns your model into a migration file
python manage.py migrate                   # creates db.sqlite3 and all tables
python manage.py loaddata sample_data      # loads catalog/fixtures/sample_data.json
```

**Expected output**

| Command | You should see |
|---|---|
| `makemigrations catalog` | `catalog\migrations\0001_initial.py` with `+ Create model Author` and `+ Create model Book` |
| `migrate` | a list of `Applying ... OK` lines, including `Applying catalog.0001_initial... OK` |
| `loaddata sample_data` | `Installed 9 object(s) from 1 fixture(s)` |

**Database after this task (pre-loaded sample data):**

`catalog_author`

| id | name | country |
|---|---|---|
| 1 | Robert C. Martin | United States |
| 2 | Martin Fowler | United Kingdom |
| 3 | Muhammad ibn Musa al-Khwarizmi | Abbasid Caliphate (Baghdad) |

`catalog_book`

| id | title | isbn | published_year | available_copies | author_id |
|---|---|---|---|---|---|
| 1 | Clean Code | 9780000000011 | 2008 | 3 | 1 |
| 2 | The Clean Coder | 9780000000028 | 2011 | 0 | 1 |
| 3 | Clean Architecture | 9780000000035 | 2017 | 2 | 1 |
| 4 | Refactoring | 9780000000042 | 1999 | 4 | 2 |
| 5 | Patterns of Enterprise Application Architecture | 9780000000059 | 2002 | 1 | 2 |
| 6 | The Compendious Book on Calculation by Completion and Balancing | 9780000000066 | 820 | 0 | 3 |

> ISBNs are sample values for this exercise.

Optional: open `db.sqlite3` in **DB Browser for SQLite** → *Browse Data* → table `catalog_book` to see the rows.
Close DB Browser before running Django commands again (otherwise you may see *database is locked*).

**Acceptance criteria**
- [ ] `python manage.py migrate` reports **No migrations to apply** when you run it a second time.
- [ ] `loaddata` installed 9 objects.

**If `loaddata` fails** with *"no such column"* or *"has no field named ..."*, a field name in Task 1 does not match
the table above. Fix the model, delete `db.sqlite3` and `catalog/migrations/0001_initial.py`, and repeat Task 2.

---

## Task 3: Use the data (admin + ORM)

### 3A: Admin

**File:** `catalog/admin.py`. Find `TODO [Day 1 · Task 3A]`.

Register `Book` with a `BookAdmin` class (`AuthorAdmin` is given as the pattern):

| Option | Value |
|---|---|
| `list_display` | `id`, `title`, `author`, `published_year`, `available_copies` |
| `list_filter` | `author` |
| `search_fields` | `title`, `isbn` |

Then:

```bash
python manage.py createsuperuser     # any username / password: local exercise only
python manage.py runserver
```

Open http://127.0.0.1:8000/admin/ → **Books**.

**Expected result:** 6 books in a table with the 5 columns above, a filter by author on the right, and a search box.
Searching `clean` shows 3 books. Filtering by *Martin Fowler* shows 2 books.

**Database change:** `createsuperuser` adds 1 row to `auth_user`. Books and authors are unchanged.

### 3B: ORM practice

**File:** `orm_practice.py`. Complete functions 1-3 (core); 4-5 are stretch. They are marked `TODO [Day 1 · Task 3B-n]`. Each function's docstring
states its expected result. Stop the server (Ctrl+C) or use a second terminal, then run:

```bash
python orm_practice.py
```

| # | Function | Level | ORM skill | Input | Expected output |
|---|---|---|---|---|---|
| 1 | `count_books()` | **core** | `.count()` | none | `6` |
| 2 | `titles_by_author(name)` | **core** | filter across a ForeignKey (`author__name`) + `order_by` | `"Martin Fowler"` | `["Patterns of Enterprise Application Architecture", "Refactoring"]` |
| 3 | `count_published_after(year)` | **core** | `__gt` lookup | `2005` | `3` |
| 4 | `available_titles()` | stretch | `__gt` lookup + `values_list` | none | 4 titles A-Z (see docstring) |
| 5 | `create_update_delete_book()` | stretch | `create()`, `save()`, `delete()` | none | `(1, 6)` |

**Database change in #5:** a temporary row is inserted (7 books), updated (`available_copies` 2 → 1), and deleted
(6 books again). After the script, the table is exactly as listed in Task 2.

**Acceptance criteria**
- [ ] Admin shows both models with the requested columns, filter, and search.
- [ ] Core: `python orm_practice.py` prints `Core:    3/3 passed`.
- [ ] *Stretch:* `Stretch: 2/2 passed`.

---

## Done? Check yourself

- [ ] I can explain what `makemigrations` creates and what `migrate` does.
- [ ] I can explain why `author` is a `ForeignKey` and what `related_name="books"` gives me.
- [ ] Now apply the same ideas to the project: [`../project-milestone.md`](../project-milestone.md)
