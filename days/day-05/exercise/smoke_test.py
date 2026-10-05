"""
Day 5 exercise - Task 3: a production smoke test for the reading-list API.

A smoke test is a SHORT check against a RUNNING server: "is the deployed system basically alive and correct?"
It sends real HTTP requests with the `requests` library (installed from the root requirements.txt).

BEFORE YOU START
    * Terminal 1 (this folder): the server is running with the sample data loaded
          python manage.py migrate
          python manage.py loaddata sample_data
          python manage.py runserver
    * Terminal 2 (this folder):
          python smoke_test.py                                        # defaults to http://127.0.0.1:8000
          python smoke_test.py --base-url https://<some-app>.onrender.com

DATA IT USES (sample data, exercise-only demo accounts)
    alice / alice-pass-2026   owns reading-list items for books 1 and 4
    bob   / bob-pass-2026     owns a reading-list item for book 3
    The test adds book 2 ("The Clean Coder") to alice's list and deletes it again -> the database ends unchanged.

EXPECTED OUTPUT when everything is done:   7/7 checks passed
"""
import argparse
import sys

import requests

TIMEOUT = 60  # seconds - a sleeping free Render service can take a while to wake up
RESULTS = []


def check(name, condition):
    """GIVEN - record and print one PASS/FAIL line."""
    RESULTS.append(bool(condition))
    print(f"[{'PASS' if condition else 'FAIL'}] {name}")


def auth_headers(token):
    """GIVEN - the header every protected request needs."""
    return {"Authorization": f"Token {token}"}


def list_requires_auth(base_url):
    """GIVEN EXAMPLE - GET the list WITHOUT a token and return the status code (expected 401)."""
    response = requests.get(f"{base_url}/api/reading-list/", timeout=TIMEOUT)
    return response.status_code


def get_token(base_url, username, password):
    """Return the token string for this user, or None if login failed.
    Request:  POST {base_url}/api/auth/token/   JSON {"username": ..., "password": ...}
    Expected: 200  {"token": "<40 characters>"}"""
    # TODO [Day 5 · Task 3a]: Send the request with requests.post(url, json={...}, timeout=TIMEOUT).
    #   Return response.json()["token"] when the status is 200, otherwise None.
    # HINT: days/day-05/hints.md#task-3  |  Example: days/day-05/example/smoke_example.py
    # YOUR CODE HERE
    return None


def create_item(base_url, token, book_id):
    """Add a book to the token owner's reading list. Return (status_code, response_json).
    Request:  POST {base_url}/api/reading-list/   JSON {"book": book_id}   + auth header
    Expected: 201  {"id": <new id>, "user": "alice", "book": 2, ...}"""
    # TODO [Day 5 · Task 3b]
    # YOUR CODE HERE
    return None, None


def get_item_status(base_url, token, item_id):
    """GET one reading-list item with this token and return ONLY the status code.
    Expected: 200 for the owner, 404 for any other user."""
    # TODO [Day 5 · Task 3c]
    # YOUR CODE HERE
    return None


def delete_item(base_url, token, item_id):
    """DELETE one reading-list item and return the status code.  Expected: 204"""
    # TODO [Day 5 · Task 3d]
    # YOUR CODE HERE
    return None


def main():
    """GIVEN - the smoke-test scenario. Do not edit."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:8000")
    base_url = parser.parse_args().base_url.rstrip("/")
    print(f"Smoke testing {base_url}\n")

    check("1. GET /api/reading-list/ without token -> 401", list_requires_auth(base_url) == 401)

    alice = get_token(base_url, "alice", "alice-pass-2026")
    bob = get_token(base_url, "bob", "bob-pass-2026")
    check("2. alice and bob can log in and receive tokens", alice and bob)
    if not (alice and bob):
        sys.exit("Cannot continue without tokens.")

    status_code, item = create_item(base_url, alice, book_id=2)
    check("3. alice adds book 2 -> 201, user is alice", status_code == 201 and item and item.get("user") == "alice")
    if status_code != 201:
        sys.exit(f"Cannot continue: create returned {status_code} {item}")

    check("4. alice can read her new item -> 200", get_item_status(base_url, alice, item["id"]) == 200)
    check("5. bob cannot read alice's item -> 404", get_item_status(base_url, bob, item["id"]) == 404)
    check("6. alice deletes her item -> 204", delete_item(base_url, alice, item["id"]) == 204)
    check("7. the deleted item is gone -> 404", get_item_status(base_url, alice, item["id"]) == 404)

    print(f"\n{sum(RESULTS)}/{len(RESULTS)} checks passed")
    sys.exit(0 if all(RESULTS) else 1)


if __name__ == "__main__":
    main()
