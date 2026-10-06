# Day 3 Hints

Open the hints **one level at a time**. Level 3 is close to the answer.

**Exercise:** [Task 1](#task-1) · [Task 2](#task-2) · [Task 3](#task-3)
**Project:** [P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6)

---

## Exercise

<a id="task-1"></a>
### Task 1: Token authentication

<details><summary>Level 1: nudge</summary>

Three separate edits, all shown in [`example/settings_and_urls.py`](example/settings_and_urls.py):
the app in `INSTALLED_APPS`, the authentication classes in `REST_FRAMEWORK`, and the login URL (import + path).
Run `python manage.py migrate` after the first edit.
</details>

<details><summary>Level 2: common errors</summary>

| Symptom | Cause |
|---|---|
| `RuntimeError: Model class rest_framework.authtoken.models.Token doesn't declare an explicit app_label` | you imported `obtain_auth_token` before adding `rest_framework.authtoken` to `INSTALLED_APPS` |
| `no such table: authtoken_token` | you did not run `migrate` after adding the app |
| `403` instead of `401` without a token | `SessionAuthentication` is listed **before** `TokenAuthentication` |
| `401 Invalid token.` | header typo: it must be exactly `Authorization: Token <key>` (word "Token", one space) |
| `400 Unable to log in with provided credentials.` | wrong username/password: they are case-sensitive |
</details>

<a id="task-2"></a>
### Task 2: Ownership

<details><summary>Level 1: nudge</summary>

Replace the class attribute `queryset = ...all()` with a **method** `get_queryset(self)` that filters by the user of
the current request. Add `perform_create` exactly like you did yesterday in the project.
</details>

<details><summary>Level 2: almost the answer</summary>

```python
def get_queryset(self):
    return ReadingListItem.objects.filter(user=___)

def perform_create(self, serializer):
    serializer.save(user=___)
```
</details>

<details><summary>Why 404 and not 403?</summary>

`retrieve`, `update` and `destroy` look the object up **inside** `get_queryset()`. Bob's queryset does not contain
alice's item, so for bob it does not exist → 404. The API reveals nothing about other users' data.
</details>

<a id="task-3"></a>
### Task 3: Validation

<details><summary>Level 1: nudge</summary>

DRF calls `validate_<field_name>(self, value)` automatically for each field. Raise
`serializers.ValidationError("message")` to reject, and `return value` to accept.
See [`example/serializers.py`](example/serializers.py).
</details>

<details><summary>Level 2: bigger hint</summary>

- "Today": `timezone.localdate()` (already imported). Dates compare with `<`.
- `value` may be `None` (no target date): check `value is not None` first.
- The current user inside a serializer: `self.context["request"].user`.
- `self.instance` is `None` on create and the existing item on update.
</details>

<details><summary>Level 3: almost the answer</summary>

```python
def validate_target_date(self, value):
    if value is not None and value < timezone.localdate():
        raise serializers.ValidationError("Target date cannot be in the past.")
    return value

def validate_book(self, value):
    user = self.context["request"].user
    duplicates = ReadingListItem.objects.filter(user=user, book=value)
    if self.instance is not None:
        duplicates = duplicates.exclude(pk=___)
    if duplicates.___():
        raise serializers.ValidationError("This book is already on your reading list.")
    return value
```
</details>

---

## Project

<a id="p1"></a>
### P1: `rest_framework.authtoken`

<details><summary>Level 1</summary>

One string in `INSTALLED_APPS`, then `python manage.py migrate`: you should see `Applying authtoken...`.
</details>

<a id="p2"></a>
### P2: Authentication classes

<details><summary>Level 1</summary>

```python
"DEFAULT_AUTHENTICATION_CLASSES": [
    "rest_framework.authentication.TokenAuthentication",
    "rest_framework.authentication.___",
],
```
Token **first**: anonymous requests then get `401` as required by the API contract.
</details>

<a id="p3"></a>
### P3: Token endpoint

<details><summary>Level 1</summary>

Part 1 is an import, part 2 is a `path(...)` line. Both are shown in
[`example/settings_and_urls.py`](example/settings_and_urls.py). The URL name must be `api-token`: the Day 4 tests use it.
</details>

<details><summary>Test it</summary>

Postman: `POST {{base_url}}/api/auth/token/`, Body → raw → JSON `{"username": "alice", "password": "..."}` → `200`
`{"token": "..."}`. Save it in the `token` environment variable (see `setup/postman.md`).
</details>

<a id="p4"></a>
### P4: `get_queryset`

<details><summary>Level 1</summary>

Delete the `queryset = Task.objects.all()` stub and write a method that returns only the tasks whose `owner` is the
current user. See [`example/views.py`](example/views.py).
</details>

<details><summary>Level 2</summary>

```python
def get_queryset(self):
    return Task.objects.filter(owner=___)
```
</details>

<a id="p5"></a>
### P5 (stretch): `IsOwner`

<details><summary>Level 1</summary>

`has_object_permission` receives the task as `obj`. Compare its owner with `request.user` and return the result
(`True` or `False`). See [`example/permissions.py`](example/permissions.py).
</details>

<a id="p6"></a>
### P6 (stretch): Owner as username (Day 2 review)

<details><summary>Level 1</summary>

Same technique as `author_name` in the Day 2 exercise: a `ReadOnlyField` with a `source` that follows the relation.
Declare it **above** `class Meta` and keep the name `owner`.
</details>
