# Day 4 Worked Example: Personal Notes API + Configuration

Read-only example files for a "personal notes" API in which every user only sees their own notes, plus a short
example of settings read from environment variables.

| File | Shows |
|---|---|
| [`settings_and_urls.py`](settings_and_urls.py) | `rest_framework.authtoken`, authentication classes (and why their order matters), the token endpoint |
| [`views.py`](views.py) | function views that filter every query by `request.user`, `get_own_note()` (another user's note → 404), `save(author=request.user)` |
| [`serializers.py`](serializers.py) | a read-only `author` field; `context={"request": request}` so a validator can see the current user |
| [`settings_env.py`](settings_env.py) | reading strings, booleans, integers and lists from environment variables |

## Authentication vs authorization

| Question | Mechanism | Fails with |
|---|---|---|
| **Who** are you? (authentication) | `Authorization: Token <key>` header → `TokenAuthentication` | **401 Unauthorized**: no or invalid credentials |
| **May** you do this? (authorization) | permission classes (`IsAuthenticated`, …) | **403 Forbidden**: identified, but not allowed |
| Does it exist **for you**? | the query is filtered by `request.user` | **404 Not Found**: another user's object is invisible |

In this program another user's object returns **404, not 403**. With 403 the API would confirm that the id exists;
404 reveals nothing.

## Defense in depth: three layers

1. `IsAuthenticated`: anonymous requests are rejected (401) before the view runs.
2. Every query contains the owner: `Note.objects.filter(author=request.user)` for lists,
   `get_object_or_404(Note, pk=pk, author=request.user)` for one object. Write that lookup **once**, in a helper
   (`get_own_note`), and use it in every view, so no view can forget it.
3. `save(author=request.user)` + a read-only author field: a client can never choose or change the owner.

## Try the token flow with Postman

1. `POST {{base_url}}/api/auth/token/` with body `{"username": "alice", "password": "..."}` → copy `token`.
2. Any protected request → tab **Headers** → `Authorization` = `Token <paste>` (note the word `Token` and the space).
3. Remove the header → 401. Use bob's token on alice's note → 404.

## Configuration belongs in the environment

The same code runs on your laptop and on Render; only the **configuration** differs. Values that change between
environments, or are secret, are read from environment variables (see [`settings_env.py`](settings_env.py)):

| Setting | Laptop | Production |
|---|---|---|
| `SECRET_KEY` | a development default is fine | a long random value, **never** in Git |
| `DEBUG` | `True` | `False` (otherwise error pages leak code and settings) |
| `ALLOWED_HOSTS` | `127.0.0.1,localhost` | `my-app.onrender.com` |

`.env.example` documents every variable with **placeholder** values and is committed. Real values are never committed.
