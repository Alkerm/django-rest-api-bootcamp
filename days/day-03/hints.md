# Day 3 Hints

Open the hints **one level at a time**. Level 3 is close to the answer.

**Exercise:** [Task 1](#task-1) · [Task 2](#task-2) · [Task 3](#task-3) · [Task 4 (stretch)](#task-4)
**Project:** [P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7 (stretch)](#p7)

---

## Exercise

<a id="task-1"></a>
### Task 1: `BookSerializer`

<details><summary>Level 1: nudge</summary>

`AuthorSerializer` right above is complete. `BookSerializer` has the same `Meta` shape, plus one extra field
declared **above** `class Meta`. Compare `AuthorSerializer` with yesterday's `author_to_dict`: `fields` is the list of
keys you used to type by hand.
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

<details><summary>Common errors</summary>

| Symptom | Cause |
|---|---|
| `ImproperlyConfigured: Field name 'author_name' is not valid` | `author_name` is in `fields` but not declared above `Meta` |
| `author_name` is missing from the JSON | declared, but not listed in `fields` |
</details>

<a id="task-2"></a>
### Task 2: The views with the serializer

<details><summary>Level 1: nudge</summary>

`list_authors` is the pattern for reading. For writing, every view follows three lines: build the serializer,
`is_valid()`, then `errors` (400) or `save()` (201/200). See [`example/views.py`](example/views.py). Delete the
`return Response(status=status.HTTP_501_NOT_IMPLEMENTED)` placeholder in each view.
</details>

<details><summary>Level 2: bigger hint</summary>

| You pass | The serializer does |
|---|---|
| `BookSerializer(book)` | object → `.data` (one dict) |
| `BookSerializer(books, many=True)` | queryset → `.data` (a list) |
| `BookSerializer(data=request.data)` | validate input → `save()` **creates** |
| `BookSerializer(book, data=request.data, partial=...)` | validate input → `save()` **updates** `book` |
</details>

<details><summary>Level 3: almost the answer</summary>

```python
serializer = BookSerializer(data=request.data)
if not serializer.is_valid():
    return Response(serializer.___, status=status.HTTP_400_BAD_REQUEST)
serializer.save()
return Response(serializer.___, status=status.HTTP_201_CREATED)
```
For `update_book`: `partial=request.method == "PATCH"`.
</details>

<details><summary>Common errors</summary>

| Symptom | Cause |
|---|---|
| `AssertionError: You must call .is_valid() before accessing .data` (or `.save()`) | call `is_valid()` first |
| PATCH with one field returns 400 | `partial` is missing or `False` for PATCH |
| PUT creates a new book instead of changing it | the existing `book` was not passed as the first argument |
| `501 Not Implemented` | the placeholder line is still at the top of the view |
</details>

<a id="task-3"></a>
### Task 3: Validation

<details><summary>Level 1: nudge</summary>

Two different tools:
- **3a** changes the *text* of an error DRF already produces: `extra_kwargs` inside `class Meta`, with
  `error_messages` for the field.
- **3b** adds a *new rule*: a method named `validate_<field_name>(self, value)` on the serializer (not inside `Meta`).
See [`example/serializers.py`](example/serializers.py).
</details>

<details><summary>Level 2: almost the answer</summary>

```python
class Meta:
    ...
    extra_kwargs = {"title": {"error_messages": {"blank": "Title cannot be blank."}}}

def validate_published_year(self, value):
    if value > timezone.localdate().___:
        raise serializers.ValidationError("Published year cannot be in the future.")
    return value
```
`timezone` is already imported at the top of the file.
</details>

<details><summary>Common errors</summary>

| Symptom | Cause |
|---|---|
| The rule never runs | the method name must be exactly `validate_published_year`, and it must be indented inside `BookSerializer`, not inside `Meta` |
| This year is rejected too | use `>` (later than this year), not `>=` |
| Everything returns 400 now | you forgot `return value` at the end of the method |
</details>

<a id="task-4"></a>
### Task 4 (stretch): Object-level rule

<details><summary>Level 1: nudge</summary>

`validate(self, attrs)` runs after every field passed. `attrs` is a dict of the validated fields. On PATCH a field
may be missing, so take it from `self.instance` (the book being edited). When editing, exclude the book itself from
the duplicate search. See `validate` in [`example/serializers.py`](example/serializers.py).
</details>

<details><summary>Level 2: almost the answer</summary>

```python
def validate(self, attrs):
    title = attrs.get("title", self.instance.title if self.instance else None)
    author = attrs.get("author", self.instance.author if self.instance else None)
    same = Book.objects.filter(title__iexact=title, author=author)
    if self.instance is not None:
        same = same.exclude(pk=___)
    if same.exists():
        raise serializers.ValidationError("This author already has a book with this title.")
    return ___
```
</details>

---

## Project

<a id="p1"></a>
### P1: `TaskSerializer` fields

<details><summary>Level 1</summary>

`fields` is the list of keys from yesterday's `task_to_dict`, in the same order. The 4 fields the server controls go in
`read_only_fields`. The `owner` is one of them: the client must never choose it.
</details>

<details><summary>Level 2</summary>

```python
fields = ["id", "title", "description", "status", "due_date", "owner", "created_at", "updated_at"]
read_only_fields = ["id", "owner", ___, ___]
```
</details>

<a id="p2"></a>
### P2: `list_tasks` + `get_task`

<details><summary>Level 1</summary>

Replace `task_to_dict(...)` with `TaskSerializer(...).data` (and `many=True` for the list). Delete `task_to_dict`
from your own code if you still have it: nothing uses it any more.
</details>

<a id="p3"></a>
### P3: `create_task`

<details><summary>Level 1</summary>

The exercise's `create_book`, with one difference: the owner is a server-side value, so it goes into `save()`:
`serializer.save(owner=request.user)`. `owner` is read-only, so a value in the body is ignored.
</details>

<details><summary>Error: <code>NOT NULL constraint failed: tasks_task.owner_id</code></summary>

`serializer.save()` was called without `owner=request.user`.
</details>

<a id="p4"></a>
### P4: `update_task`

<details><summary>Level 1</summary>

The exercise's `update_book`: `TaskSerializer(task, data=request.data, partial=request.method == "PATCH")`.
</details>

<a id="p5"></a>
### P5: Title error messages

<details><summary>Level 1</summary>

`extra_kwargs` sets options for fields that `ModelSerializer` generates. The option you need is `error_messages`, a
dictionary from error code (`"required"`, `"blank"`) to text.
</details>

<details><summary>Level 2</summary>

```python
extra_kwargs = {
    "title": {
        "error_messages": {
            "required": "Title is required.",
            "blank": "___",
        }
    }
}
```
It goes **inside** `class Meta`. See `extra_kwargs` in [`example/serializers.py`](example/serializers.py).
</details>

<a id="p6"></a>
### P6: Due date not in the past (on create)

<details><summary>Level 1</summary>

Write `validate_due_date(self, value)`. Three conditions must all be true to reject: it is a create
(`self.instance is None`), a date was given (`value is not None`), and it is before `timezone.localdate()`.
`validate_release_date` in [`example/serializers.py`](example/serializers.py) is the same idea.
</details>

<details><summary>Level 2</summary>

```python
def validate_due_date(self, value):
    if self.instance is None and value is not None and value < ___:
        raise serializers.ValidationError("Due date cannot be earlier than today.")
    return ___
```
</details>

<a id="p7"></a>
### P7 (stretch): Owner as username

<details><summary>Level 1</summary>

Declare the field above `class Meta`, like `added_by` in [`example/serializers.py`](example/serializers.py):
`owner = serializers.ReadOnlyField(source="owner.___")`. It stays read-only, so P3 still sets it from `request.user`.
</details>
