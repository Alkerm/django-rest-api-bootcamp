# Day 2 Exercise: Book CRUD API (Serializers, ViewSets, Routers)

| | |
|---|---|
| **What you will practice** | Writing a `ModelSerializer` (including a read-only related field) · building a `ModelViewSet` · registering it with a router · exercising all six CRUD operations and reading their status codes |
| **Where to start** | This folder: `days/day-02/exercise/`. Files: `catalog/serializers.py` → `catalog/views.py` → `catalog/urls.py` → `catalog/models.py` → `crud_checklist.md` |
| **Result to produce** | **Core:** a working `/api/books/` API with all six operations, sorted A-Z; `python manage.py test` → **Ran 9 tests ... OK**. **Stretch:** the completed `crud_checklist.md` |
| **Time** | ~50 minutes |
| **Hints** | [`../hints.md`](../hints.md) · worked example: [`../example/`](../example/) |

---

## Before you start

Run these in a terminal **opened in this folder** (`days/day-02/exercise`):

```bash
..\..\..\.venv\Scripts\Activate.ps1          # Windows PowerShell
source ../../../.venv/bin/activate            # macOS

python manage.py migrate                      # creates this exercise's db.sqlite3 and its tables
python manage.py loaddata sample_data         # -> Installed 9 object(s) from 1 fixture(s)
python manage.py runserver                    # keep it running; use a 2nd terminal for other commands
```

> **Your progress meter:** `python manage.py test` (in the 2nd terminal). At the start most tests fail: that is
> expected. Each failure says which task fixes it. Check one task at a time with `python manage.py test -k task1`.

> **Database state: pre-filled with sample data.** After the commands above, the database contains **3 authors and
> 6 books** (tables below). The API is **open (no login)** today, so you can focus on CRUD. Authentication comes on Day 3.

This exercise has its **own** database: `days/day-02/exercise/db.sqlite3`. To reset it at any time:
`python manage.py flush --no-input` then `python manage.py loaddata sample_data`.

**Given and ready:** models and migrations, `AuthorSerializer` + `AuthorViewSet` (`GET /api/authors/`) as a complete
example, and `/api/` routing in `config/urls.py`. Open http://127.0.0.1:8000/api/authors/ now: it already works.

---

## Task 1: `BookSerializer`

**File:** `catalog/serializers.py`. Find `TODO [Day 2 · Task 1a]` and `TODO [Day 2 · Task 1b]`.

The serializer converts a `Book` row to JSON and validates incoming JSON. The data it works with:

**Table `catalog_book`**

| Field | Type | Rules | In the JSON |
|---|---|---|---|
| `id` | BigAutoField (PK) | automatic | read-only |
| `title` | CharField(200) | required, not blank | writable |
| `isbn` | CharField(13) | required, **unique** | writable |
| `published_year` | PositiveIntegerField | required, ≥ 0 | writable |
| `available_copies` | PositiveIntegerField | default 1 | writable (optional) |
| `author` | ForeignKey → `catalog_author.id` | must be an existing author id | writable: send the id, e.g. `2` |
| `created_at` | DateTimeField | set automatically on create | read-only |
| `author_name` | **not a column**: comes from `book.author.name` | none | read-only |

**Expected output** for `GET /api/books/1/` (once Task 2 is done):

```json
{
  "id": 1,
  "title": "Clean Code",
  "isbn": "9780000000011",
  "published_year": 2008,
  "available_copies": 3,
  "author": 1,
  "author_name": "Robert C. Martin",
  "created_at": "2026-10-01T12:01:00+03:00"
}
```

**Acceptance criteria**
- [ ] The JSON keys appear in exactly this order.
- [ ] Sending `id` or `created_at` in a request body has no effect.

---

## Task 2: `BookViewSet` + router

**Files:** `catalog/views.py` (`TODO [Day 2 · Task 2a]`) and `catalog/urls.py` (`TODO [Day 2 · Task 2b]`).

Create a viewset with **all six** operations and register it as `books`. The router then generates:

| Operation | Method + URL | Success status |
|---|---|---|
| list | `GET /api/books/` | 200 |
| create | `POST /api/books/` | 201 |
| retrieve | `GET /api/books/{id}/` | 200 (unknown id → 404) |
| update | `PUT /api/books/{id}/` | 200 |
| partial_update | `PATCH /api/books/{id}/` | 200 |
| destroy | `DELETE /api/books/{id}/` | 204 |

**Sample rows you can use** (pre-loaded):

| id | title | isbn | published_year | available_copies | author (id → name) |
|---|---|---|---|---|---|
| 1 | Clean Code | 9780000000011 | 2008 | 3 | 1 → Robert C. Martin |
| 2 | The Clean Coder | 9780000000028 | 2011 | 0 | 1 → Robert C. Martin |
| 3 | Clean Architecture | 9780000000035 | 2017 | 2 | 1 → Robert C. Martin |
| 4 | Refactoring | 9780000000042 | 1999 | 4 | 2 → Martin Fowler |
| 5 | Patterns of Enterprise Application Architecture | 9780000000059 | 2002 | 1 | 2 → Martin Fowler |
| 6 | The Compendious Book on Calculation by Completion and Balancing | 9780000000066 | 820 | 0 | 3 → Muhammad ibn Musa al-Khwarizmi |

**Try it:** open http://127.0.0.1:8000/api/books/. You should see 6 books and a form to POST a new one.

**Acceptance criteria**
- [ ] http://127.0.0.1:8000/api/ lists both `authors` and `books`.
- [ ] `python manage.py test` passes every `test_task1_*` and `test_task2_*` test.

---

## Task 3: Order the list, then prove every operation

### 3A: Sort books A-Z (Day 1 review)

**File:** `catalog/models.py`. Find `TODO [Day 2 · Task 3A]`. Add `Meta.ordering = ["title"]`, then:

```bash
python manage.py makemigrations catalog     # -> 0002_... "Change Meta options on book"
python manage.py migrate
```

**Database change:** none to the rows. The migration only records the new default ordering.
**Expected output:** `GET /api/books/` now starts with *Clean Architecture, Clean Code, Patterns of ...*

### 3B (STRETCH, optional): CRUD checklist

> The project milestone has its own 7-request check, so do this one only if you finish early.

Work through [`crud_checklist.md`](crud_checklist.md): 9 requests, each with its body, expected status and expected
database change. Record the actual status, then answer the 3 questions at the bottom.

**Acceptance criteria**
- [ ] `python manage.py test` → `Ran 9 tests ... OK`.
- [ ] *Stretch:* every row of `crud_checklist.md` has an actual status that matches the expected one.

---

## Done? Check yourself

- [ ] I can explain why `PUT` with one field returns 400 but `PATCH` with one field returns 200.
- [ ] I can explain what the router generated for me (look at http://127.0.0.1:8000/api/).
- [ ] Now apply the same ideas to the project: [`../project-milestone.md`](../project-milestone.md)
