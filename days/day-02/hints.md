# Day 2 Hints

Open the hints **one level at a time**. Level 3 is close to the answer.

**Exercise:** [Task 1](#task-1) · [Task 2](#task-2) · [Task 3](#task-3)
**Project:** [P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6)

---

## Exercise

<a id="task-1"></a>
### Task 1: `BookSerializer`

<details><summary>Level 1: nudge</summary>

`AuthorSerializer` right above is complete. `BookSerializer` has the same `Meta` shape, plus one extra field
declared **above** `class Meta`.
</details>

<details><summary>Level 2: bigger hint</summary>

- A value that comes from a related object: `serializers.ReadOnlyField(source="relation.attribute")`
- Every name you want in the JSON must appear in `fields`, **including** the extra field you declared.
- `read_only_fields` lists fields the client cannot set.
- See [`example/serializers.py`](example/serializers.py) (`director_name`).
</details>

<details><summary>Level 3: almost the answer</summary>

```python
author_name = serializers.ReadOnlyField(source="author.___")

class Meta:
    model = Book
    fields = ["id", "title", "isbn", "published_year", "available_copies", "author", "author_name", "created_at"]
    read_only_fields = [___, ___]
```
</details>

<a id="task-2"></a>
### Task 2: `BookViewSet` + router

<details><summary>Level 1: nudge</summary>

`AuthorViewSet` only reads (`ReadOnlyModelViewSet`). Which viewset class also creates, updates and deletes?
The router line for authors in `urls.py` is your pattern.
</details>

<details><summary>Level 2: bigger hint</summary>

```python
class BookViewSet(viewsets.___):
    queryset = Book.objects.___()
    serializer_class = ___
```
Remove the stub class (the one with `pass`) when you write yours. Then in `urls.py`:
`router.register("books", BookViewSet, basename="book")`.
</details>

<details><summary>Common errors</summary>

| Symptom | Cause |
|---|---|
| `/api/books/` → 404 | the router registration is missing, or a typo in the prefix |
| `405 Method Not Allowed` on POST | still a read-only / generic viewset |
| `AssertionError: 'BookViewSet' should either include a serializer_class attribute...` | missing `serializer_class` |
| `ImproperlyConfigured: Field name 'author_name' is not valid` | `author_name` is in `fields` but not declared above `Meta` |
</details>

<a id="task-3"></a>
### Task 3: Ordering + CRUD checklist

<details><summary>Level 1: ordering</summary>

```python
class Meta:
    ordering = ["___"]
```
Indent it **inside** `Book`, at the same level as the fields. Then run `makemigrations` and `migrate`.
</details>

<details><summary>Level 2: sending requests in the browsable API</summary>

- `GET` and `POST`: open http://127.0.0.1:8000/api/books/. The form at the bottom has a **Raw data** tab: paste the
  JSON and click **POST**.
- `PUT`, `PATCH`, `DELETE`: open http://127.0.0.1:8000/api/books/7/. The **DELETE** button is at the top. PUT/PATCH
  use the raw-data form at the bottom.
- Postman: choose the method, URL, **Body → raw → JSON**.
</details>

---

## Project

<a id="p1"></a>
### P1: `Meta.ordering` (Day 1 review)

<details><summary>Level 1</summary>

Same idea as the exercise's Task 3A, but the newest first: a `-` in front of the field name means descending.
Afterwards: `python manage.py makemigrations` → `0002_...` and `python manage.py migrate`.
</details>

<a id="p2"></a>
### P2: `TaskSerializer` fields

<details><summary>Level 1</summary>

All 8 fields go in `fields`. The 4 fields the server controls go in `read_only_fields`. The `owner` is one of them:
the client must never choose it.
</details>

<details><summary>Level 2</summary>

```python
fields = ["id", "title", "description", "status", "due_date", "owner", "created_at", "updated_at"]
read_only_fields = ["id", "owner", ___, ___]
```
</details>

<a id="p3"></a>
### P3: `TaskViewSet` queryset + serializer

<details><summary>Level 1</summary>

Two class attributes, exactly like `MovieViewSet` in [`example/views.py`](example/views.py).
</details>

<a id="p4"></a>
### P4: `perform_create`

<details><summary>Level 1</summary>

DRF calls `perform_create(self, serializer)` after validation. Call `serializer.save(...)` and pass the owner as a
keyword argument. The logged-in user is `self.request.user`.
</details>

<details><summary>Level 2</summary>

```python
def perform_create(self, serializer):
    serializer.save(owner=___)
```
</details>

<details><summary>Error: <code>NOT NULL constraint failed: tasks_task.owner_id</code></summary>

`perform_create` is missing or does not pass `owner=`.
</details>

<a id="p5"></a>
### P5: Router

<details><summary>Level 1</summary>

`router.register(prefix, ViewSet, basename=...)`. See [`example/urls.py`](example/urls.py).
</details>

<a id="p6"></a>
### P6: Project URLs

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
