# Day 1 Hints

Open the hints **one level at a time**. Try for a few minutes after each level before opening the next one.
Level 3 is close to the answer: use it to get unblocked, then make sure you understand every line.

**Exercise:** [Task 1](#task-1) · [Task 2](#task-2) · [Task 3](#task-3)
**Project:** [P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [Commands](#project-commands)

---

## Exercise

<a id="task-1"></a>
### Task 1: Complete the `Book` model

<details><summary>Level 1: nudge</summary>

Look at `Author` just above `Book`. Every field is `name = models.SomeField(options)`.
The table in the exercise README gives you the name, the type and the options of each field.
</details>

<details><summary>Level 2: bigger hint</summary>

- Text with a maximum length → `models.CharField(max_length=...)`
- Whole numbers ≥ 0 → `models.PositiveIntegerField()`
- Uniqueness → add `unique=True`; a default value → add `default=...`
- `__str__` must **return** a string: which attribute holds the title?
</details>

<details><summary>Level 3: almost the answer</summary>

```python
title = models.CharField(max_length=200)
isbn = models.CharField(max_length=13, unique=True)
published_year = models.PositiveIntegerField()
available_copies = models.PositiveIntegerField(default=___)

def __str__(self):
    return self.___
```
</details>

<a id="task-2"></a>
### Task 2: Migrations and sample data

<details><summary>Level 1: nudge</summary>

Run the three commands **in order**, inside `days/day-01/exercise`, with the `(.venv)` prefix visible in your prompt.
</details>

<details><summary>Level 2: common errors</summary>

| Error | Meaning |
|---|---|
| `No changes detected` | the model has no new fields: did you save `models.py`? |
| `no such table: catalog_book` | you skipped `migrate` |
| `Problem installing fixture ... has no field named 'X'` | a field name in your model differs from the README table (spelling!) |
| `You are trying to add a non-nullable field ...` | you migrated before finishing Task 1. Choose option 2 (quit), delete `db.sqlite3` and the files in `catalog/migrations/` **except `__init__.py`**, then repeat. |
| `ModuleNotFoundError: No module named 'django'` | the virtual environment is not active |
</details>

<a id="task-3"></a>
### Task 3: Admin and ORM

<details><summary>Level 1: nudge (admin)</summary>

`AuthorAdmin` is the pattern. Copy it, rename it to `BookAdmin`, register it for `Book`, and change the lists.
</details>

<details><summary>Level 2: nudge (ORM)</summary>

Every function starts with `Book.objects.` Pick the method:
`count()` · `filter(field=value)` · `filter(field__gt=value)` · `filter(author__name=...)` · `order_by("title")` ·
`values_list("title", flat=True)` · `create(...)` · `obj.save()` · `obj.delete()`.
See [`example/orm_examples.py`](example/orm_examples.py).
</details>

<details><summary>Level 3: almost the answer</summary>

```python
# 2
books = Book.objects.filter(author__name=author_name).order_by("title")
return [book.title for book in books]

# 4
return list(Book.objects.filter(available_copies__gt=___).order_by("title").values_list("title", flat=True))

# 5
fowler = Author.objects.get(name="Martin Fowler")
book = Book.objects.create(title="Temporary Book", isbn="9789999999999",
                           published_year=2026, available_copies=2, author=fowler)
book.available_copies -= 1
book.save()
book.refresh_from_db()
copies = book.available_copies
book.delete()
return copies, Book.objects.___()
```
</details>

---

## Project

<a id="p1"></a>
### P1: `INSTALLED_APPS` (`config/settings.py`)

<details><summary>Level 1</summary>

Two strings are missing: the Python package name of Django REST Framework, and the name of the app you created
with `startapp`.
</details>

<details><summary>Level 2</summary>

```python
    "rest_framework",
    "___",          # the folder name of your app
```
</details>

<a id="p2"></a>
### P2: Status choices (`tasks/models.py`)

<details><summary>Level 1</summary>

Inside a `TextChoices` class, each line is `CONSTANT = "STORED_VALUE", "Human label"`.
See `Genre` in [`example/models.py`](example/models.py).
</details>

<details><summary>Level 2</summary>

```python
TODO = "TODO", "To do"
IN_PROGRESS = "___", "In progress"
DONE = "___", "___"
```
Remove the `pass` line once you have real lines.
</details>

<a id="p3"></a>
### P3: Task fields (`tasks/models.py`)

<details><summary>Level 1</summary>

The TODO comment has a table with every field. `id` is automatic; do not write it.
Use `settings.AUTH_USER_MODEL` (already imported) for the owner.
</details>

<details><summary>Level 2</summary>

```python
title = models.CharField(max_length=200)
description = models.TextField(blank=True)
status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)
due_date = models.DateField(null=True, blank=True)
owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.___, related_name="tasks")
created_at = models.DateTimeField(auto_now_add=___)
updated_at = models.DateTimeField(auto_now=___)
```
</details>

<a id="p4"></a>
### P4: `__str__`

<details><summary>Level 1</summary>

Use an f-string with `self.title` and `self.get_status_display()`.
</details>

<a id="p5"></a>
### P5: Admin (`tasks/admin.py`)

<details><summary>Level 1</summary>

Use the `@admin.register(Task)` decorator on a `TaskAdmin(admin.ModelAdmin)` class.
See [`example/admin.py`](example/admin.py).
</details>

<details><summary>Level 2</summary>

```python
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "status", "due_date", "owner", "created_at"]
    list_filter = [___, ___]
    search_fields = [___]
```
</details>

<a id="project-commands"></a>
### Commands after P1-P5

<details><summary>Show the commands</summary>

```bash
python manage.py makemigrations tasks     # -> tasks\migrations\0001_initial.py  + Create model Task
python manage.py migrate
python manage.py createsuperuser          # your admin account
python manage.py runserver                # http://127.0.0.1:8000/admin/
```
In the admin: **Users → Add user** twice (e.g. `alice`, `bob`), then **Tasks → Add task** a few times for each owner.
Stop the server, start it again, and confirm the tasks are still there.
</details>
