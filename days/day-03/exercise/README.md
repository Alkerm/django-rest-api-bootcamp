# Day 3 Exercise: Book API with a Serializer (Serialization + Validation)

| | |
|---|---|
| **What you will practice** | Writing a `ModelSerializer` (including a read-only related field) · using it in function views (`many=True`, `is_valid()`, `errors`, `save()`, `partial`) · adding validation rules with clear error messages |
| **Where to start** | This folder: `days/day-03/exercise/`. Files: `catalog/serializers.py` (Task 1) → `catalog/views.py` (Task 2) → `catalog/serializers.py` again (Task 3) → stretch: Task 4 in `catalog/serializers.py` |
| **Result to produce** | **Core (Tasks 1-3):** the same five book URLs as yesterday, now serialized and validated; every row of the **self-check** table at the bottom passes. **Stretch (Task 4):** an object-level rule |
| **Time** | ~50 minutes for the core |
| **Hints** | [`../hints.md`](../hints.md) · worked example: [`../example/`](../example/) |

---

## Before you start

Run these in a terminal **opened in this folder** (`days/day-03/exercise`):

```bash
..\..\..\.venv\Scripts\Activate.ps1          # Windows PowerShell
source ../../../.venv/bin/activate            # macOS

python manage.py migrate                      # creates this exercise's db.sqlite3 and its tables
python manage.py loaddata sample_data         # -> Installed 9 object(s) from 1 fixture(s)
python manage.py runserver                    # keep it running; use a 2nd terminal for other commands
```

> **Database state: pre-filled with sample data.** The same **3 authors and 6 books** as yesterday (books sorted A-Z).
> The API is still **open (no login)**. Authentication comes on Day 4.

This exercise has its **own** database: `days/day-03/exercise/db.sqlite3`. To reset it at any time:
`python manage.py flush --no-input` then `python manage.py loaddata sample_data`.

**Given and ready:** models, migrations, the five URLs in `catalog/urls.py` (exactly yesterday's), `AuthorSerializer`
+ `list_authors` as a complete example, and `delete_book` (it needs no serializer). The views you rewrite answer
`501 Not Implemented` until you replace their placeholder line.

**Why today?** Yesterday's `create_book` only checked that fields were present. A duplicate isbn crashed with a 500,
and a text like `"abc"` for `published_year` slipped through to the database. Today's serializer turns all of those
into a clean `400` with a message per field.

---

## Task 1: `BookSerializer`

**File:** `catalog/serializers.py`. Find `TODO [Day 3 · Task 1a]` and `TODO [Day 3 · Task 1b]`.

The serializer replaces yesterday's `book_to_dict()`: it converts a `Book` row to JSON **and** validates incoming
JSON. The data it works with:

**Table `catalog_book`**

| Field | Type | Rules (checked by the serializer for free) | In the JSON |
|---|---|---|---|
| `id` | BigAutoField (PK) | automatic | read-only |
| `title` | CharField(200) | required, not blank, ≤ 200 characters | writable |
| `isbn` | CharField(13) | required, **unique** | writable |
| `published_year` | PositiveIntegerField | required, a number ≥ 0 | writable |
| `available_copies` | PositiveIntegerField | default 1 | writable (optional) |
| `author` | ForeignKey → `catalog_author.id` | must be an existing author id | writable: send the id, e.g. `2` |
| `created_at` | DateTimeField | set automatically on create | read-only |
| `author_name` | **not a column**: comes from `book.author.name` | none | read-only |

**Try it in the shell** (`python manage.py shell`), before Task 2:

```python
from catalog.models import Book
from catalog.serializers import BookSerializer
BookSerializer(Book.objects.get(pk=1)).data      # -> {'id': 1, 'title': 'Clean Code', ... 'author_name': 'Robert C. Martin', ...}
s = BookSerializer(data={"title": "", "author": 999})
s.is_valid(), s.errors                           # -> (False, {'title': [...], 'isbn': [...], 'published_year': [...], 'author': [...]})
```

**Acceptance criteria**
- [ ] The JSON keys appear in exactly yesterday's order: `id, title, isbn, published_year, available_copies, author, author_name, created_at`.

---

## Task 2: Use the serializer in the views

**File:** `catalog/views.py`. Find `TODO [Day 3 · Task 2a]` … `2d`.

| View | Method + URL (unchanged) | With the serializer |
|---|---|---|
| `list_books` | `GET /api/books/` | `BookSerializer(books, many=True).data` |
| `get_book` | `GET /api/books/{id}/` | `BookSerializer(book).data` |
| `create_book` | `POST /api/books/create/` | `BookSerializer(data=request.data)` → `is_valid()` → 400 or `save()` + 201 |
| `update_book` | `PUT` / `PATCH /api/books/{id}/update/` | `BookSerializer(book, data=request.data, partial=...)` |

**Expected input → output**

| Request | Expected response | Database change |
|---|---|---|
| `POST /api/books/create/` `{"title": "Domain-Driven Design", "isbn": "9780000000073", "published_year": 2003, "available_copies": 2, "author": 2}` | `201`, id 7 | new row |
| `POST /api/books/create/` `{"title": "", "isbn": "9780000000011", "published_year": -5, "author": 999}` | `400`, errors for **all four** fields (the duplicate isbn too) | none |
| `PUT /api/books/1/update/` `{"title": "Only a title"}` | `400`: PUT needs every required field | none |
| `PATCH /api/books/2/update/` `{"available_copies": 7}` | `200`, only copies changed | row 2 |

**Acceptance criteria**
- [ ] Nothing in `views.py` builds a dict by hand any more.
- [ ] An invalid POST returns `400` with field errors and saves nothing.

---

## Task 3: Validation (the serializer as gatekeeper)

**File:** `catalog/serializers.py`. Find `TODO [Day 3 · Task 3a]` and `TODO [Day 3 · Task 3b]`.

DRF already rejects many bad inputs for you (missing fields, wrong types, a duplicate `isbn`, an unknown author).
Now you add the library's own rules and make one built-in message clearer:

| Rule | Field | Error message (exact) |
|---|---|---|
| 3a: a blank title gets a clear message (built-in rule, custom text via `extra_kwargs`) | `title` | `Title cannot be blank.` |
| 3b: `published_year` cannot be later than this year (this year is fine) | `published_year` | `Published year cannot be in the future.` |

**Expected input → output** (`POST /api/books/create/`)

| Request | Expected response | Database change |
|---|---|---|
| `{"title": "   ", "isbn": "9780000000097", "published_year": 2020, "author": 1}` | `400` `{"title": ["Title cannot be blank."]}` | none |
| `{"title": "From the future", "isbn": "9780000000103", "published_year": 2099, "author": 1}` | `400` `{"published_year": ["Published year cannot be in the future."]}` | none |
| `{"title": "Brand new", "isbn": "9780000000110", "published_year": 2026, "author": 1}` | `201` | new book row |

---

## Task 4 (STRETCH, optional): An object-level rule

**File:** `catalog/serializers.py`. Find `TODO [Day 3 · Task 4`.

An author cannot have two books with the same title (case does not matter). The rule needs **two** fields at once, so
it goes in `validate(self, attrs)`, not in a `validate_<field>` method.

| Request | Expected response |
|---|---|
| `POST /api/books/create/` `{"title": "clean code", "isbn": "9780000000127", "published_year": 2020, "author": 1}` | `400` `{"non_field_errors": ["This author already has a book with this title."]}` |
| `PATCH /api/books/1/update/` `{"available_copies": 9}` | `200`: a book does not clash with itself |

---

## Self-check (core)

Reset the data first (`flush` + `loaddata`, see above), then:

| # | Request | Expected |
|---|---|---|
| 1 | `GET /api/books/1/` | `200`, 8 keys including `"author_name": "Robert C. Martin"` |
| 2 | `POST /api/books/create/` with the Domain-Driven Design body | `201`, id 7 |
| 3 | `POST /api/books/create/` `{"id": 99, "title": "X", "isbn": "9780000000080", "published_year": 2020, "author": 1}` | `201`, id is **not** 99 |
| 4 | `POST /api/books/create/` with the four-error body from Task 2 | `400`, four fields with errors |
| 5 | `PUT /api/books/1/update/` `{"title": "Only a title"}` | `400` |
| 6 | `PATCH /api/books/2/update/` `{"available_copies": 7}` | `200` |
| 7 | the three Task 3 requests | `400`, `400`, `201` with the exact messages |

## Done? Check yourself

- [ ] I can explain why `PUT` with one field returns 400 but `PATCH` with one field returns 200 (`partial`).
- [ ] I can explain what `serializer.is_valid()` checks, and where each error message comes from.
- [ ] I can explain the difference between a built-in rule, a `validate_<field>` method and `validate()`.
- [ ] Now apply the same ideas to the project: [`../project-milestone.md`](../project-milestone.md)
