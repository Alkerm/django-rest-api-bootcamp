# Day 4 Worked Example: Testing and Configuration

| File | Shows |
|---|---|
| [`test_notes_api.py`](test_notes_api.py) | `APITestCase`, `setUp`, tokens in tests, success / failure / validation / authentication tests, checking the database with `refresh_from_db()` |
| [`settings_env.py`](settings_env.py) | reading strings, booleans, integers and lists from environment variables |

## Reading a failing test

```text
FAIL: test_other_user_cannot_edit_note (notes.tests.NoteAPITests.test_other_user_cannot_edit_note)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../notes/tests.py", line 41, in test_other_user_cannot_edit_note
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
AssertionError: 200 != 404
```

Read it from the bottom up:

1. **`AssertionError: 200 != 404`**: the API returned 200, but the test expected 404.
2. **line 41**: which assertion failed.
3. **the test name**: which behaviour is broken ("other user cannot edit note").

Conclusion: the application lets another user edit the note, which is a security bug. **Fix the application**
(here: `get_queryset()`), never weaken the test's expectation.

`ERROR` (instead of `FAIL`) means the test crashed before its assertion, e.g. a typo, a missing URL name, or an
exception in the view. Read the last line of the traceback first.

## Commands

```bash
python manage.py test                       # all tests
python manage.py test -v 2                  # list every test with ok / FAIL / ERROR / skipped
python manage.py test tasks.tests.TaskAPITests.test_delete_own_task     # one test
```

## What makes a test "meaningful"?

- It checks the **status code** *and* the important part of the **body** or **database**.
- It covers **both** directions: allowed work succeeds, forbidden or invalid work fails **and changes nothing**.
- It does not depend on other tests or on your local `db.sqlite3` (data comes from `setUp`).
