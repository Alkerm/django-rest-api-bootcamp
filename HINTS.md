# Hints

Open the hints **one level at a time**. Level 2 is close to the answer. The worked examples are in
[`examples/`](examples/).

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [P8](#p8) · [P9](#p9) ·
[P10](#p10) · [P11 (stretch)](#p11) · [Common errors](#errors)

---

<a id="p1"></a>
### P1: `Meta.ordering`

<details><summary>Level 1</summary>

An inner `class Meta` inside `Task`, at the same indentation as the fields. A `-` in front of the field name means
descending (newest first). See `Meta` in [`examples/day-01/models.py`](examples/day-01/models.py).
</details>

<details><summary>Level 2</summary>

```python
class Meta:
    ordering = ["___"]
```
Then run `python manage.py makemigrations` (→ `0002_alter_task_options.py`) and `python manage.py migrate`.
</details>

<a id="p2"></a>
### P2: `TaskSerializer` fields

<details><summary>Level 1</summary>

`fields` is the list of keys the JSON shows, in order. `read_only_fields` are the ones the client may see but never
set: the server controls them. The `owner` is one of them: a client must never choose it.
See [`examples/day-03/serializers.py`](examples/day-03/serializers.py).
</details>

<details><summary>Level 2</summary>

```python
fields = ["id", "title", "description", "status", "due_date", "owner", "created_at", "updated_at"]
read_only_fields = ["id", "owner", ___, ___]
```
Delete the placeholder line `fields = ["id"]`.
</details>

<a id="p3"></a>
### P3: Title error messages

<details><summary>Level 1</summary>

`extra_kwargs` sets options for fields that `ModelSerializer` generates. The option you need is `error_messages`, a
dictionary from error code (`"required"`, `"blank"`) to text. It goes **inside** `class Meta`.
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
</details>

<a id="p4"></a>
### P4: Due date not in the past (on create)

<details><summary>Level 1</summary>

Write a method `validate_due_date(self, value)` on the serializer (not inside `Meta`). Three conditions must all be
true to reject: it is a create (`self.instance is None`), a date was given (`value is not None`), and it is before
`timezone.localdate()`. `validate_release_date` in [`examples/day-03/serializers.py`](examples/day-03/serializers.py)
is the same idea.
</details>

<details><summary>Level 2</summary>

```python
def validate_due_date(self, value):
    if self.instance is None and value is not None and value < ___:
        raise serializers.ValidationError("Due date cannot be earlier than today.")
    return ___
```
</details>

<a id="p5"></a>
### P5: `list_tasks` + `get_task`

<details><summary>Level 1</summary>

Delete the placeholder `return Response(status=status.HTTP_501_NOT_IMPLEMENTED)`. Query the rows with the ORM, give
them to the serializer, return `.data`. See `list_movies` and `get_movie` in
[`examples/day-03/views.py`](examples/day-03/views.py).
</details>

<details><summary>Level 2</summary>

| You pass | You get |
|---|---|
| `TaskSerializer(task)` | `.data` = one dict |
| `TaskSerializer(tasks, many=True)` | `.data` = a list of dicts |

```python
tasks = Task.objects.all()
return Response(TaskSerializer(tasks, many=___).data)

task = get_object_or_404(Task, pk=pk)          # unknown id -> 404
return Response(TaskSerializer(task).___)
```
</details>

<a id="p6"></a>
### P6: `create_task`

<details><summary>Level 1</summary>

Three steps: build the serializer with `data=request.data`, call `is_valid()`, then either return the errors (400)
or save (201). The owner is a server-side value: pass it to `save()`. The logged-in user is `request.user`.
</details>

<details><summary>Level 2</summary>

```python
serializer = TaskSerializer(data=request.data)
if not serializer.is_valid():
    return Response(serializer.___, status=status.HTTP_400_BAD_REQUEST)
serializer.save(owner=___)
return Response(serializer.data, status=status.HTTP_201_CREATED)
```
</details>

<a id="p7"></a>
### P7: `update_task`

<details><summary>Level 1</summary>

Like P6, but pass the **existing** task first, so `save()` updates it instead of creating a new one:
`TaskSerializer(task, data=request.data, partial=...)`. `partial` is `True` for PATCH and `False` for PUT.
</details>

<details><summary>Level 2</summary>

```python
task = get_object_or_404(Task, pk=pk)
serializer = TaskSerializer(task, data=request.data, partial=request.method == "___")
if not serializer.is_valid():
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
serializer.save()
return Response(serializer.data)
```
</details>

<a id="p8"></a>
### P8: `delete_task`

<details><summary>Level 1</summary>

Find the task (or 404), `task.delete()`, then `Response(status=status.HTTP_204_NO_CONTENT)`: no data, just the
status. See `delete_movie` in [`examples/day-02/views.py`](examples/day-02/views.py).
</details>

<a id="p9"></a>
### P9: Task URLs

<details><summary>Level 1</summary>

`path("url/", views.function, name="name")`, one line per view, inside `urlpatterns`. `<int:pk>` captures the id
from the URL and passes it to the view as `pk`. See [`examples/day-02/urls.py`](examples/day-02/urls.py).
</details>

<details><summary>Level 2</summary>

```python
path("tasks/", views.list_tasks, name="task-list"),
path("tasks/create/", views.___, name="task-create"),
path("tasks/<int:pk>/", views.get_task, name="___"),
path("tasks/<int:pk>/update/", views.update_task, name="task-update"),
path("tasks/<int:pk>/delete/", views.delete_task, name="task-delete"),
```
</details>

<a id="p10"></a>
### P10: Project URLs

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

<a id="p11"></a>
### P11 (stretch): Owner as username

<details><summary>Level 1</summary>

Declare the field **above** `class Meta`, like `added_by` in
[`examples/day-03/serializers.py`](examples/day-03/serializers.py):
`owner = serializers.ReadOnlyField(source="owner.___")`. It stays read-only, so P6 still sets it from `request.user`.
</details>

---

<a id="errors"></a>
## Common errors

| Symptom | Cause / fix |
|---|---|
| `501 Not Implemented` | the placeholder `return` line is still at the top of the view |
| `403 Authentication credentials were not provided` | you are not logged in: http://127.0.0.1:8000/api-auth/login/ |
| `/api/tasks/` → 404 | P9 or P10 missing, or a typo / missing trailing `/` in a path |
| `405 Method Not Allowed` | wrong URL for that method: POST → `/create/`, PUT/PATCH → `/update/`, DELETE → `/delete/` |
| `NOT NULL constraint failed: tasks_task.owner_id` | `serializer.save()` without `owner=request.user` (P6) |
| `You must call .is_valid() before accessing .data` | call `is_valid()` first |
| PATCH with one field → 400 | `partial` missing or `False` for PATCH (P7) |
| PUT creates a new task instead of changing it | the existing `task` was not passed as the first argument (P7) |
| The validation rule never runs | method not named exactly `validate_due_date`, or indented inside `Meta` (P4) |
| `TypeError ... unexpected keyword argument` | the converter name differs from the view argument: `<int:pk>` ↔ `pk` |
| `No changes detected` after P1 | file not saved, or `Meta` is not indented inside `Task` |
| `ModuleNotFoundError: No module named 'django'` | the `.venv` is not active: run setup step 8 again |
