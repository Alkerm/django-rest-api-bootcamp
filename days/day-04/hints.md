# Day 4 Hints

Open the hints **one level at a time**. Level 3 is close to the answer.

**Exercise:** [Task 1](#task-1) · [Task 2 (stretch)](#task-2)
**Project:** [P2 tests](#p2) · [P3 settings](#p3) · [P4 .env.example](#p4) · [P5 requirements](#p5)

---

## Exercise

<a id="task-1"></a>
### Task 1: Writing the tests

<details><summary>Level 1: nudge</summary>

Copy the shape of the complete example test: (optional) `self.use_token(...)` → **one** request → assertions.
The table in the exercise README tells you the request and the expected result of every test.
See [`example/test_notes_api.py`](example/test_notes_api.py).
</details>

<details><summary>Level 2: building blocks</summary>

```python
self.use_token(self.alice_token)                                   # act as alice
response = self.client.get(url)
response = self.client.post(url, {"book": self.book_2.id}, format="json")
response = self.client.patch(url, {"status": "FINISHED"}, format="json")
response = self.client.delete(url)

self.assertEqual(response.status_code, status.HTTP_201_CREATED)   # 200 OK, 204 NO_CONTENT, 400 BAD_REQUEST, 404 NOT_FOUND
self.assertIn("target_date", response.data)                        # error reported for this field
self.alice_item.refresh_from_db()                                  # re-read before checking the database
self.assertTrue(ReadingListItem.objects.filter(id=...).exists())
```
</details>

<details><summary>Level 3: one test written out</summary>

```python
def test_other_users_item_returns_404(self):
    self.use_token(self.bob_token)
    response = self.client.get(self.alice_item_url)
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
```
</details>

<details><summary>Common errors</summary>

| Symptom | Cause |
|---|---|
| test still shows as `skipped` | the `self.skipTest(...)` line is still there: delete it (fine for STRETCH tests you skip on purpose) |
| `KeyError: 'token'` | the login failed: check the password used in `setUp` |
| `401` where you expected `200` | you forgot `self.use_token(...)` in this test (each test starts logged out) |
| `AssertionError: 'READING' != 'FINISHED'` after a PATCH | call `refresh_from_db()` before reading the object |
| `IntegrityError: UNIQUE constraint failed` | you created a book with an ISBN that `setUp` already uses |
</details>

<a id="task-2"></a>
### Task 2 (stretch): Break it on purpose

<details><summary>Level 1</summary>

Look for lines starting with `FAIL:` in the output. Each gives the test name. The `AssertionError: X != Y` line
shows what the API returned (X) vs. what the test expected (Y).
</details>

---

## Project

<a id="p2"></a>
### P2: The project tests (`tasks/tests.py`)

<details><summary>Level 1: nudge</summary>

`setUp` gives you `self.alice`, `self.bob`, their tokens, one task each (`self.alice_task`, `self.bob_task`), and the
URLs. `self.authenticate(token)` logs in for the current test. Each TODO says what to send and what to assert.
</details>

<details><summary>Level 2: the three tests built together with the instructor</summary>

```python
def test_create_assigns_owner_from_token(self):
    self.authenticate(self.alice_token)
    response = self.client.post(self.list_url, {"title": "New task", "owner": self.bob.id}, format="json")
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response.data["owner"], "alice")
    self.assertEqual(Task.objects.get(id=response.data["id"]).owner, self.alice)

def test_cannot_retrieve_another_users_task(self):
    self.authenticate(self.alice_token)
    response = self.client.get(self.bob_detail_url)
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
```
</details>

<details><summary>Level 3: dates in tests</summary>

```python
tomorrow = timezone.localdate() + timedelta(days=1)
yesterday = timezone.localdate() - timedelta(days=1)
payload = {"title": "Late", "due_date": yesterday.isoformat()}   # "2026-10-13"
```
</details>

<a id="p3"></a>
### P3: Settings from the environment

<details><summary>Level 1</summary>

Three lines with `os.getenv(name, default)`: see [`example/settings_env.py`](example/settings_env.py). Use the
project's default `"development-only-key"` for `SECRET_KEY`.
Delete the three stub lines below `# YOUR CODE HERE`. After the change, `python manage.py runserver` and
`python manage.py test` must still work **without** setting any variable.
</details>

<a id="p4"></a>
### P4: `.env.example`

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

<a id="p5"></a>
### P5: Deployment packages

<details><summary>Level 1</summary>

```bash
python -m pip install "psycopg[binary]>=3.2,<4" gunicorn whitenoise dj-database-url
python -m pip check
```
Then add one line per package to `requirements.txt` (with a version range), or regenerate it with
`python -m pip freeze > requirements.txt`. Render installs exactly what this file lists.
</details>
