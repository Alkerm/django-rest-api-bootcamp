# Day 4 Hints

Open the hints **one level at a time**. Level 3 is close to the answer.

**Exercise:** [Task 1](#task-1) · [Task 2](#task-2) · [Task 3](#task-3)
**Project:** [P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [P8](#p8)

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

Three small edits, all about `request.user` (the user the token belongs to):
- **2a** the list: filter instead of `.all()`.
- **2b** the helper that finds ONE item: add the user to the lookup.
- **2c** create: pass the user to `save()`, exactly like the owner in your project.

See `list_notes`, `get_own_note` and `create_note` in [`example/views.py`](example/views.py).
</details>

<details><summary>Level 2: almost the answer</summary>

```python
items = ReadingListItem.objects.filter(user=___).select_related("book")      # 2a

return get_object_or_404(ReadingListItem, pk=pk, user=___)                     # 2b

serializer.save(user=___)                                                      # 2c
```
</details>

<details><summary>Why 404 and not 403?</summary>

`get_own_item()` looks the item up with **both** the id and the user. Bob has no item with id 1, so for bob it does
not exist → 404. The API reveals nothing about other users' data. And because get, update and delete all use the same
helper, one fix protects all three.
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
[`example/settings_and_urls.py`](example/settings_and_urls.py). The URL name must be `api-token`.
</details>

<details><summary>Test it</summary>

Postman: `POST {{base_url}}/api/auth/token/`, Body → raw → JSON `{"username": "alice", "password": "..."}` → `200`
`{"token": "..."}`. Save it in the `token` environment variable (see `setup/postman.md`).
</details>

<a id="p4"></a>
### P4: Only my tasks in the list

<details><summary>Level 1</summary>

Delete the `tasks = Task.objects.all()` stub and filter by the owner instead. See `list_notes` in
[`example/views.py`](example/views.py).
</details>

<details><summary>Level 2</summary>

```python
tasks = Task.objects.filter(owner=___)
```
</details>

<a id="p5"></a>
### P5: `get_own_task`

<details><summary>Level 1</summary>

`get_task`, `update_task` and `delete_task` already call `get_own_task()`. Today it finds **any** task by id. Add the
owner to the lookup, and another user's task becomes a 404 everywhere at once.
</details>

<details><summary>Level 2</summary>

```python
return get_object_or_404(Task, pk=pk, owner=___)
```
</details>

<a id="p6"></a>
### P6: Settings from the environment

<details><summary>Level 1</summary>

Three lines with `os.getenv(name, default)`: see [`example/settings_env.py`](example/settings_env.py). Use the
project's default `"development-only-key"` for `SECRET_KEY`.
Delete the three stub lines below `# YOUR CODE HERE`. After the change, `python manage.py runserver` must still work **without** setting any variable.
</details>

<a id="p7"></a>
### P7: `.env.example`

<details><summary>Level 1</summary>

```text
# Long random string - generate with:
#   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
SECRET_KEY=replace-with-a-long-random-value
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
```
Placeholders only. Check that `.env` (the real one, if you create it) is in `.gitignore`.
</details>

<a id="p8"></a>
### P8: Deployment packages (given)

<details><summary>Level 1</summary>

The final checkpoint already lists the four deployment packages in `requirements.txt` (exact versions, tested by the
instructor team):

```text
psycopg[binary]==3.3.6
dj-database-url==3.1.2
gunicorn==26.2.0
whitenoise==6.12.0
```

You installed them in the copy step. Check that nothing is broken:

```bash
python -m pip install -r requirements.txt
python -m pip check
```
Render installs exactly what this file lists, so your laptop and production run the same versions.
</details>
