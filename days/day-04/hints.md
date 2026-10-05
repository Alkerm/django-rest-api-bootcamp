# Day 4 Hints

Open the hints **one level at a time**. Level 3 is close to the answer.

**Exercise:** [Task 1](#task-1) · [Task 2](#task-2) · [Task 3](#task-3)
**Project:** [P2 tests](#p2) · [P3 settings](#p3) · [P4 .env.example](#p4) · [P5 requirements](#p5) · [P6 README](#p6)

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
### Task 2: Settings from the environment

<details><summary>Level 1: nudge</summary>

`os.getenv("NAME", "default")` always returns **text**. Convert it: compare lower-cased text with `"true"` for a
bool, and `split(",")` for a list. See [`example/settings_env.py`](example/settings_env.py).
</details>

<details><summary>Level 2: almost the answer</summary>

```python
SECRET_KEY = os.getenv("SECRET_KEY", "exercise-only-key")
DEBUG = os.getenv("DEBUG", "True").lower() == ___
ALLOWED_HOSTS = [host.strip() for host in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",") if host.strip()]
```
`.env.example` lines look like `NAME=placeholder`, with a `# comment` above each one.
</details>

<details><summary>Why is <code>bool(os.getenv("DEBUG"))</code> wrong?</summary>

`bool("False")` is `True`: any non-empty string is truthy. Production would run with `DEBUG` on.
</details>

<a id="task-3"></a>
### Task 3: Break it on purpose

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

Exactly the same three lines as the exercise's Task 2, with the project's default `"development-only-key"`.
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

<a id="p6"></a>
### P6: README

<details><summary>Level 1</summary>

Write for a classmate who has never seen your project. Each `_TODO_` section needs real commands or examples that
**work when copied**. The test: swap repositories with a partner, follow only the README, and note every place where
they got stuck.
</details>

<details><summary>Level 2: checklist from the program brief</summary>

The README must cover: setup, environment variables, migrations, test command, authentication, endpoint examples,
deployed URL (Day 5), and project decisions.
</details>
