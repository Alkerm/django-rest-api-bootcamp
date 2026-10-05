# Day 3 Worked Example: Personal Notes API

Read-only example files for a "personal notes" API in which every user only sees their own notes.

| File | Shows |
|---|---|
| [`settings_and_urls.py`](settings_and_urls.py) | `rest_framework.authtoken`, authentication classes (and why their order matters), the token endpoint |
| [`views.py`](views.py) | `get_queryset()` filtered by `request.user`, `perform_create()` setting the owner |
| [`permissions.py`](permissions.py) | object-level permissions (`has_object_permission`) |
| [`serializers.py`](serializers.py) | built-in, field-level (`validate_<field>`), and object-level (`validate`) validation; `self.instance` and `self.context["request"]` |

## Authentication vs authorization

| Question | Mechanism | Fails with |
|---|---|---|
| **Who** are you? (authentication) | `Authorization: Token <key>` header → `TokenAuthentication` | **401 Unauthorized**: no or invalid credentials |
| **May** you do this? (authorization) | permission classes (`IsAuthenticated`, `IsAuthor`, …) | **403 Forbidden**: identified, but not allowed |
| Does it exist **for you**? | `get_queryset()` filtered by user | **404 Not Found**: another user's object is invisible |

In this program another user's object returns **404, not 403**. With 403 the API would confirm that the id exists;
404 reveals nothing.

## Defense in depth: four layers

1. `IsAuthenticated`: anonymous requests are rejected (401).
2. `get_queryset()`: lists and lookups only ever contain the caller's rows (404 for others).
3. Object permission (`IsAuthor`): a second check in case a future view forgets layer 2.
4. `perform_create()` + read-only owner field: a client can never choose or change the owner.

## Try the token flow with Postman

1. `POST {{base_url}}/api/auth/token/` with body `{"username": "alice", "password": "..."}` → copy `token`.
2. Any protected request → tab **Headers** → `Authorization` = `Token <paste>` (note the word `Token` and the space).
3. Remove the header → 401. Use bob's token on alice's note → 404.
