"""
Production smoke test for the Task Management API.

A short confidence check against a RUNNING server (local or deployed). It verifies:
    401 without token -> token login for two users -> create -> list -> partial update
    -> validation error (400) -> cross-user isolation (404) -> delete (204) -> deleted task is gone (404)

It only uses the Python standard library, and it cleans up the task it creates.
Passwords are typed at the prompt (or read from SMOKE_PASSWORD / SMOKE_OTHER_PASSWORD) and never stored.

Usage:
    python smoke_test.py --base-url http://127.0.0.1:8000 --user alice --other-user bob
    python smoke_test.py --base-url https://<your-app>.onrender.com --user alice --other-user bob
"""
import argparse
import getpass
import json
import os
import sys
import urllib.error
import urllib.request

RESULTS = []


def call(base_url, method, path, token=None, body=None):
    """Send one JSON request and return (status_code, parsed_json_or_None)."""
    data = json.dumps(body).encode() if body is not None else None
    request = urllib.request.Request(base_url.rstrip("/") + path, data=data, method=method)
    request.add_header("Accept", "application/json")
    if data is not None:
        request.add_header("Content-Type", "application/json")
    if token:
        request.add_header("Authorization", f"Token {token}")
    try:
        with urllib.request.urlopen(request, timeout=90) as response:  # free Render services may need to wake up
            raw = response.read()
            return response.status, json.loads(raw) if raw else None
    except urllib.error.HTTPError as error:
        raw = error.read()
        try:
            return error.code, json.loads(raw) if raw else None
        except json.JSONDecodeError:
            return error.code, None


def check(name, condition, detail=""):
    RESULTS.append(condition)
    print(f"[{'PASS' if condition else 'FAIL'}] {name}" + (f"  ({detail})" if detail and not condition else ""))
    return condition


def get_token(base_url, username, password):
    status, body = call(base_url, "POST", "/api/auth/token/", body={"username": username, "password": password})
    check(f"POST /api/auth/token/ as {username} -> 200 + token", status == 200 and body and "token" in body, status)
    return (body or {}).get("token")


def main():
    parser = argparse.ArgumentParser(description="Smoke-test the Task Management API.")
    parser.add_argument("--base-url", required=True, help="e.g. http://127.0.0.1:8000")
    parser.add_argument("--user", required=True, help="first test user (creates the task)")
    parser.add_argument("--other-user", required=True, help="second test user (must NOT see the task)")
    args = parser.parse_args()

    password = os.getenv("SMOKE_PASSWORD") or getpass.getpass(f"Password for {args.user}: ")
    other_password = os.getenv("SMOKE_OTHER_PASSWORD") or getpass.getpass(f"Password for {args.other_user}: ")
    base = args.base_url
    print(f"Smoke testing {base}\n")

    status, _ = call(base, "GET", "/api/tasks/")
    check("GET /api/tasks/ without token -> 401", status == 401, status)

    token = get_token(base, args.user, password)
    other_token = get_token(base, args.other_user, other_password)
    if not (token and other_token):
        print("\nCannot continue without two valid tokens.")
        sys.exit(1)

    status, task = call(base, "POST", "/api/tasks/", token, {"title": "Smoke test task", "status": "TODO"})
    check("POST /api/tasks/ -> 201, owner set by server", status == 201 and task["owner"] == args.user, status)
    task_id = task["id"] if status == 201 else None
    if task_id is None:
        print("\nCannot continue without a created task.")
        sys.exit(1)

    status, tasks = call(base, "GET", "/api/tasks/", token)
    check("GET /api/tasks/ -> 200 and contains the new task", status == 200 and any(t["id"] == task_id for t in tasks), status)

    status, body = call(base, "PATCH", f"/api/tasks/{task_id}/", token, {"status": "DONE"})
    check("PATCH /api/tasks/{id}/ -> 200, status DONE", status == 200 and body["status"] == "DONE", status)

    status, body = call(base, "POST", "/api/tasks/", token, {"title": "   ", "status": "FINISHED"})
    check("POST invalid task -> 400 with field errors", status == 400 and "title" in body and "status" in body, status)

    status, _ = call(base, "GET", f"/api/tasks/{task_id}/", other_token)
    check(f"GET the task as {args.other_user} -> 404 (data isolation)", status == 404, status)

    status, _ = call(base, "DELETE", f"/api/tasks/{task_id}/", token)
    check("DELETE /api/tasks/{id}/ -> 204", status == 204, status)

    status, _ = call(base, "GET", f"/api/tasks/{task_id}/", token)
    check("GET deleted task -> 404", status == 404, status)

    passed = sum(RESULTS)
    print(f"\n{passed}/{len(RESULTS)} checks passed.")
    print("Persistence: create a task, restart/redeploy the service, and confirm it is still listed.")
    sys.exit(0 if passed == len(RESULTS) else 1)


if __name__ == "__main__":
    main()
