# Day 2 Exercise: Book CRUD API (Function Views + `path()` Routing)

| | |
|---|---|
| **What you will practice** | Converting a model object to a dict · writing one `@api_view` function per CRUD operation · reading `request.data` · returning the right status code · connecting each view to a URL with `path()` |
| **Where to start** | This folder: `days/day-02/exercise/`. Files: `catalog/views.py` (Tasks 1-3) → `catalog/urls.py` (Task 4) → stretch: `catalog/models.py`, `crud_checklist.md` |
| **Result to produce** | **Core (Tasks 1-4):** five working book endpoints; every row of the **self-check** table at the bottom passes. **Stretch (Task 5):** books sorted A-Z and the completed `crud_checklist.md` |
| **Time** | ~50 minutes for the core |
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

> **Database state: pre-filled with sample data.** After the commands above, the database contains **3 authors and
> 6 books** (tables below). The API is **open (no login)** today, so you can focus on CRUD. Authentication comes on Day 4.

This exercise has its **own** database: `days/day-02/exercise/db.sqlite3`. To reset it at any time:
`python manage.py flush --no-input` then `python manage.py loaddata sample_data`.

**Given and ready:** models and migrations, `author_to_dict` + `list_authors` (`GET /api/authors/`) as a complete
example, and `/api/` in `config/urls.py`. Open http://127.0.0.1:8000/api/authors/ now: it already works.

**Until a view is written** it answers `501 Not Implemented`. Each task replaces one of those placeholders.

---

## Task 1: `book_to_dict`

**File:** `catalog/views.py`. Find `TODO [Day 2 · Task 1]`.

A view cannot return a `Book` object directly: it must return plain Python data (dicts, lists, strings, numbers) that
DRF can turn into JSON. `book_to_dict` does that conversion. The data it works with:

**Table `catalog_book`**

| Field | Type | Rules | In the dict |
|---|---|---|---|
| `id` | BigAutoField (PK) | automatic | `book.id` |
| `title` | CharField(200) | required | `book.title` |
| `isbn` | CharField(13) | required, **unique** | `book.isbn` |
| `published_year` | PositiveIntegerField | required | `book.published_year` |
| `available_copies` | PositiveIntegerField | default 1 | `book.available_copies` |
| `author` | ForeignKey → `catalog_author.id` | must be an existing author | the id: `book.author_id` |
| `created_at` | DateTimeField | set automatically on create | `book.created_at` |
| `author_name` | **not a column**: comes from the related author | none | `book.author.name` |

**Expected output** for `GET /api/books/1/` (once Tasks 3 and 4 are done):

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
- [ ] The dict has exactly these 8 keys, in this order.

---

## Task 2: List and create

**File:** `catalog/views.py`. Find `TODO [Day 2 · Task 2a]` (`list_books`) and `TODO [Day 2 · Task 2b]` (`create_book`).

| View | Method + URL | Success | Failures |
|---|---|---|---|
| `list_books` | `GET /api/books/` | `200` + a list of all books | none |
| `create_book` | `POST /api/books/create/` | `201` + the new book | `400` when `title`, `isbn`, `published_year` or `author` is missing or empty · `404` for an unknown author id |

**Expected input → output**

| Request | Expected response | Database change |
|---|---|---|
| `POST {"title": "Domain-Driven Design", "isbn": "9780000000073", "published_year": 2003, "available_copies": 2, "author": 2}` | `201`, `"id": 7`, `"author_name": "Martin Fowler"` | new row id 7 |
| `POST {"title": ""}` | `400` `{"title": [...], "isbn": [...], "published_year": [...], "author": [...]}` | none |
| `POST {"id": 99, "title": "X", "isbn": "9780000000080", "published_year": 2020, "author": 1}` | `201`, the id is **not** 99 | new row: the server chooses the id |

**Acceptance criteria**
- [ ] `GET /api/books/` returns the 6 sample books.
- [ ] A valid POST returns `201` and the row appears in the database (admin or DB Browser).
- [ ] A POST with missing fields returns `400` and saves nothing.

---

## Task 3: Retrieve, update, delete

**File:** `catalog/views.py`. Find `TODO [Day 2 · Task 3a]`, `3b`, `3c`.

| View | Method + URL | Success | Failures |
|---|---|---|---|
| `get_book` | `GET /api/books/{id}/` | `200` + the book | `404` unknown id |
| `update_book` | `PUT` or `PATCH /api/books/{id}/update/` | `200` + the changed book | `404` |
| `delete_book` | `DELETE /api/books/{id}/delete/` | `204`, empty body | `404` |

**Sample rows you can use** (pre-loaded):

| id | title | isbn | published_year | available_copies | author (id → name) |
|---|---|---|---|---|---|
| 1 | Clean Code | 9780000000011 | 2008 | 3 | 1 → Robert C. Martin |
| 2 | The Clean Coder | 9780000000028 | 2011 | 0 | 1 → Robert C. Martin |
| 3 | Clean Architecture | 9780000000035 | 2017 | 2 | 1 → Robert C. Martin |
| 4 | Refactoring | 9780000000042 | 1999 | 4 | 2 → Martin Fowler |
| 5 | Patterns of Enterprise Application Architecture | 9780000000059 | 2002 | 1 | 2 → Martin Fowler |
| 6 | The Compendious Book on Calculation by Completion and Balancing | 9780000000066 | 820 | 0 | 3 → Muhammad ibn Musa al-Khwarizmi |

**Acceptance criteria**
- [ ] `PATCH /api/books/2/update/` with `{"available_copies": 7}` changes only `available_copies`.
- [ ] `DELETE /api/books/6/delete/` returns `204`; afterwards `GET /api/books/6/` returns `404`.

---

## Task 4: The URLs

**File:** `catalog/urls.py`. Find `TODO [Day 2 · Task 4]`.

Until now nothing calls your views: a view only runs when a URL points to it. Add one `path()` per view:

| URL (under `/api/`) | View | Name |
|---|---|---|
| `books/` | `views.list_books` | `book-list` |
| `books/create/` | `views.create_book` | `book-create` |
| `books/<int:pk>/` | `views.get_book` | `book-detail` |
| `books/<int:pk>/update/` | `views.update_book` | `book-update` |
| `books/<int:pk>/delete/` | `views.delete_book` | `book-delete` |

**Try it:** open http://127.0.0.1:8000/api/books/. You should see 6 books. Open
http://127.0.0.1:8000/api/books/create/: the page says `405 Method Not Allowed` for GET (correct: this URL only
accepts POST) and shows a form at the bottom where you can POST JSON.

**Acceptance criteria**
- [ ] Every row of the self-check below gives the expected status.

---

## Task 5 (STRETCH, optional): Order the list, then prove every operation

### 5A: Sort books A-Z (Day 1 review)

**File:** `catalog/models.py`. Find `TODO [Day 2 · Task 5`. Add `Meta.ordering = ["title"]`, then:

```bash
python manage.py makemigrations catalog     # -> 0002_alter_book_options.py "Change Meta options on book"
python manage.py migrate
```

**Database change:** none to the rows. The migration only records the new default ordering.
**Expected output:** `GET /api/books/` now starts with *Clean Architecture, Clean Code, …*

### 5B: CRUD checklist

Work through [`crud_checklist.md`](crud_checklist.md): 9 requests, each with its body, expected status and expected
database change. Record the actual status, then answer the 3 questions at the bottom.

---

## Self-check (core)

Reset the data first (`flush` + `loaddata`, see above), then send these in the browsable API or Postman:

| # | Request | Expected |
|---|---|---|
| 1 | `GET /api/books/` | `200`, 6 books |
| 2 | `POST /api/books/create/` with the Domain-Driven Design body from Task 2 | `201`, id 7 |
| 3 | `GET /api/books/7/` | `200` |
| 4 | `PATCH /api/books/7/update/` `{"available_copies": 10}` | `200`, only copies changed |
| 5 | `DELETE /api/books/7/delete/` | `204` |
| 6 | `GET /api/books/7/` | `404` |
| 7 | `POST /api/books/create/` `{"title": ""}` | `400`, nothing saved |
| 8 | `DELETE /api/books/1/` (wrong URL for delete) | `405` |

## Done? Check yourself

- [ ] I can explain what `@api_view(["GET"])` does when a POST arrives.
- [ ] I can explain how `/api/books/3/update/` reaches `update_book(request, pk=3)`.
- [ ] I can name two bad inputs that my `create_book` does **not** catch yet (look at the rules in the Task 1 table).
      Tomorrow a serializer catches them for you.
- [ ] Now apply the same ideas to the project: [`../project-milestone.md`](../project-milestone.md)
