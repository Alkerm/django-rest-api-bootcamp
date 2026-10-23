# Day 2 Hints

Open the hints **one level at a time**. Level 3 is close to the answer.

**Exercise:** [Task 1](#task-1) · [Task 2](#task-2) · [Task 3](#task-3) · [Task 4](#task-4) · [Task 5 (stretch)](#task-5)
**Project:** [P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [P8](#p8)

---

## Exercise

<a id="task-1"></a>
### Task 1: `book_to_dict`

<details><summary>Level 1: nudge</summary>

`author_to_dict` right above is complete. `book_to_dict` is the same idea with more keys. Replace the placeholder line
`return {"id": book.id}` with the full dict.
</details>

<details><summary>Level 2: bigger hint</summary>

- A column of the row: `book.title`, `book.isbn`, ...
- The id stored in a ForeignKey column: `book.author_id` (no extra query).
- A value from the related row: `book.author.name` (Django follows the relationship for you).
- See `movie_to_dict` in [`example/views.py`](example/views.py).
</details>

<details><summary>Level 3: almost the answer</summary>

```python
return {
    "id": book.id,
    "title": book.title,
    "isbn": book.___,
    "published_year": book.___,
    "available_copies": book.___,
    "author": book.author_id,
    "author_name": book.author.___,
    "created_at": book.created_at,
}
```
</details>

<a id="task-2"></a>
### Task 2: `list_books` + `create_book`

<details><summary>Level 1: nudge</summary>

`list_books` is `list_authors` with other names. `create_book` has three steps: **check** the input, **save** the
row, **answer** with 201. Delete the `return Response(status=status.HTTP_501_NOT_IMPLEMENTED)` placeholder in each view.
</details>

<details><summary>Level 2: bigger hint</summary>

```python
@api_view(["GET"])
def list_books(request):
    books = Book.objects.___()
    return Response([book_to_dict(book) for book in ___])
```

For `create_book`, `request.data` behaves like a dict: `request.data.get("title")` returns `None` when the key is
missing. Collect the errors in a dict, then return them all at once:

```python
errors = {}
for field in REQUIRED_FIELDS:
    value = request.data.get(field)
    if value is None or str(value).strip() == "":
        errors[field] = ["This field is required."]
if errors:
    return Response(errors, status=status.___)
```
</details>

<details><summary>Level 3: almost the answer (the save + answer part)</summary>

```python
author = get_object_or_404(Author, pk=request.data["author"])
book = Book.objects.create(
    title=request.data["title"],
    isbn=request.data["isbn"],
    published_year=request.data["published_year"],
    available_copies=request.data.get("available_copies", 1),
    author=___,
)
return Response(book_to_dict(book), status=status.HTTP_201_CREATED)
```
</details>

<details><summary>Common errors</summary>

| Symptom | Cause |
|---|---|
| `501 Not Implemented` | the placeholder `return` line is still there (it runs before your code) |
| `405 Method Not Allowed` on POST | you sent the POST to `/api/books/` instead of `/api/books/create/` |
| `IntegrityError: UNIQUE constraint failed: catalog_book.isbn` (500) | that isbn already exists. Correct: we do not check it yet. Day 3's serializer turns it into a 400 |
| `TypeError: Object of type Book is not JSON serializable` | you returned model objects (`Response(books)`): convert each one with `book_to_dict` |
</details>

<a id="task-3"></a>
### Task 3: `get_book`, `update_book`, `delete_book`

<details><summary>Level 1: nudge</summary>

All three start with the same line: find the book or answer 404. `get_object_or_404(Book, pk=pk)` does exactly that.
The `pk` argument comes from the URL (`<int:pk>`).
</details>

<details><summary>Level 2: bigger hint</summary>

```python
book = get_object_or_404(Book, pk=pk)
for field in UPDATABLE_FIELDS:
    if field in request.data:
        setattr(book, field, request.data[field])   # same as book.title = ..., but with the name in a variable
book.___()
return Response(book_to_dict(book))
```
Delete: `book.delete()` then `return Response(status=status.HTTP_204_NO_CONTENT)`.
</details>

<a id="task-4"></a>
### Task 4: The URLs

<details><summary>Level 1: nudge</summary>

The `authors/` line at the top of `urlpatterns` is your pattern: `path("url/", views.function, name="name")`. Put
your five lines inside the same list.
</details>

<details><summary>Level 2: almost the answer</summary>

```python
path("books/", views.list_books, name="book-list"),
path("books/create/", views.___, name="book-create"),
path("books/<int:pk>/", views.get_book, name="___"),
path("books/<int:pk>/update/", views.update_book, name="book-update"),
path("books/<int:pk>/delete/", views.delete_book, name="book-delete"),
```
</details>

<details><summary>Common errors</summary>

| Symptom | Cause |
|---|---|
| `/api/books/` → 404 | the path is missing or has a typo (check the trailing `/`) |
| `TypeError: get_book() got an unexpected keyword argument 'id'` | the converter must be named like the argument: `<int:pk>` |
| `AttributeError: module 'catalog.views' has no attribute ...` | the function name in `urls.py` does not match the one in `views.py` |
</details>

<a id="task-5"></a>
### Task 5 (stretch): Ordering + CRUD checklist

<details><summary>Level 1: ordering</summary>

```python
class Meta:
    ordering = ["___"]
```
Indent it **inside** `Book`, at the same level as the fields. Then run `makemigrations` and `migrate`.
</details>

<details><summary>Level 2: sending requests in the browsable API</summary>

- `GET`: open the URL, e.g. http://127.0.0.1:8000/api/books/7/.
- `POST`: open http://127.0.0.1:8000/api/books/create/. Ignore the 405 for GET; paste JSON in the form at the bottom
  (media type `application/json`) and click **POST**.
- `PUT`, `PATCH`: open http://127.0.0.1:8000/api/books/7/update/ and use the form at the bottom.
- `DELETE`: open http://127.0.0.1:8000/api/books/7/delete/, then click the red **DELETE** button at the top.
- Postman: choose the method, URL, **Body → raw → JSON**.
</details>

---

## Project

<a id="p1"></a>
### P1: `Meta.ordering` (Day 1 review)

<details><summary>Level 1</summary>

Same idea as the exercise's Task 5A, but the newest first: a `-` in front of the field name means descending.
Afterwards: `python manage.py makemigrations` → `0002_...` and `python manage.py migrate`.
</details>

<a id="p2"></a>
### P2: `task_to_dict`

<details><summary>Level 1</summary>

All 8 fields of the API, in the order of the TODO. The owner is shown as its id: `task.owner_id`.
</details>

<details><summary>Level 2</summary>

```python
return {
    "id": task.id,
    "title": task.title,
    "description": task.___,
    "status": task.___,
    "due_date": task.due_date,
    "owner": task.___,
    "created_at": task.created_at,
    "updated_at": task.updated_at,
}
```
</details>

<a id="p3"></a>
### P3: `list_tasks` + `create_task`

<details><summary>Level 1</summary>

The exercise's `list_books` and `create_book` are the same pattern. The only new idea: the owner comes from the logged-in
user, `request.user`, and **never** from `request.data`.
</details>

<details><summary>Level 2</summary>

```python
title = str(request.data.get("title", "")).strip()
if not title:
    return Response({"title": ["Title is required."]}, status=status.HTTP_400_BAD_REQUEST)

task = Task.objects.create(
    title=title,
    description=request.data.get("description", ""),
    status=request.data.get("status", Task.Status.TODO),
    due_date=request.data.get("due_date"),
    owner=___,
)
task.refresh_from_db()
return Response(task_to_dict(task), status=status.___)
```
`refresh_from_db()` reloads the row, so `due_date` is a real date and not the text that was sent.
</details>

<details><summary>Error: <code>NOT NULL constraint failed: tasks_task.owner_id</code></summary>

`owner=request.user` is missing in `Task.objects.create(...)`.
</details>

<a id="p4"></a>
### P4: `get_task`

<details><summary>Level 1</summary>

Two lines: `get_object_or_404(Task, pk=pk)`, then return the task as a dict.
</details>

<a id="p5"></a>
### P5: `update_task`

<details><summary>Level 1</summary>

The exercise's `update_book` loop with `UPDATABLE_FIELDS`. `owner`, `id` and the timestamps are not in the list, so
the client cannot change them. Call `task.refresh_from_db()` after `save()`, as in P3.
</details>

<a id="p6"></a>
### P6: `delete_task`

<details><summary>Level 1</summary>

Find, `delete()`, `Response(status=status.HTTP_204_NO_CONTENT)`.
</details>

<a id="p7"></a>
### P7: Task URLs

<details><summary>Level 1</summary>

Five `path()` lines inside `urlpatterns`, exactly like the exercise's Task 4, with `tasks/` and the names
`task-list`, `task-create`, `task-detail`, `task-update`, `task-delete`. See [`example/urls.py`](example/urls.py).
</details>

<a id="p8"></a>
### P8: Project URLs

<details><summary>Level 1</summary>

`include("app_name.urls")` mounts all routes of an app under a prefix. DRF's login views are
`include("rest_framework.urls")`.
</details>

<details><summary>Level 2</summary>

```python
path("api/", include("tasks.urls")),
path("api-auth/", include("___")),
```
Then log in at http://127.0.0.1:8000/api-auth/login/ and open http://127.0.0.1:8000/api/tasks/.
</details>

<details><summary><code>403 Authentication credentials were not provided</code></summary>

Expected while you are logged out: today the API requires a logged-in user. Log in at `/api-auth/login/` with one of
the users you created on Day 1.
</details>
