# Day 2 Worked Example: Movies API

Read-only example files (Movies domain, models from [`../../day-01/example/models.py`](../../day-01/example/models.py)).

| File | Shows |
|---|---|
| [`views.py`](views.py) | one **function view** per CRUD operation with `@api_view`, `request.data`, `Response(..., status=...)`, `get_object_or_404`, a hand-written `movie_to_dict()` |
| [`urls.py`](urls.py) | plain `path()` routing: one URL per view, the `<int:pk>` converter, URL names |

## What a function view is

```python
@api_view(["GET"])                 # which HTTP methods this URL accepts (others -> 405 Method Not Allowed)
def get_movie(request, pk):        # Django calls it with the request (+ values captured from the URL)
    movie = get_object_or_404(Movie, pk=pk)   # ORM query; unknown id -> 404
    return Response(movie_to_dict(movie))     # Python dict -> JSON, 200 OK
```

URL → view → ORM → database → dict → `Response` → JSON + status code. That is the whole API.

## One POST request, step by step

```text
POST /api/movies/create/  {"title": "Dune", "imdb_code": "tt1160419", "director": 1}
  │
  ├─ urls.py         → "movies/create/" matches → create_movie(request)
  ├─ @api_view       → POST allowed? (GET here → 405)   body parsed into request.data
  ├─ our checks      → title empty?  yes → 400 + {"title": ["This field is required."]}   (nothing saved)
  │                                   no ↓
  ├─ ORM             → Movie.objects.create(..., added_by=request.user)  → INSERT row
  └─ Response        → 201 Created + movie_to_dict(movie) as JSON (including id and created_at)
```

## The CRUD contract

| Action | Method + URL | View | Success | Typical failures |
|---|---|---|---|---|
| list | `GET /api/movies/` | `list_movies` | 200 + array | none |
| create | `POST /api/movies/create/` | `create_movie` | 201 + object | 400 invalid body |
| retrieve | `GET /api/movies/{id}/` | `get_movie` | 200 + object | 404 unknown id |
| update | `PUT /api/movies/{id}/update/` | `update_movie` | 200 + object | 400, 404 |
| partial update | `PATCH /api/movies/{id}/update/` | `update_movie` | 200 + object | 400, 404 |
| delete | `DELETE /api/movies/{id}/delete/` | `delete_movie` | 204, empty body | 404 |

Using the wrong method on a URL (for example `DELETE /api/movies/3/`) returns **405 Method Not Allowed**.

## PUT vs PATCH

Stored movie: `{"title": "Dune", "genre": "DRAMA", "imdb_code": "tt1160419", "director": 1}`

| Request | Meaning |
|---|---|
| `PATCH {"genre": "COMEDY"}` | "change only these fields": only `genre` changes |
| `PUT {...every field...}` | "here is the whole new object": every field is replaced |

Today both go to the same view and only the fields that were sent are changed. On Day 3 the serializer makes PUT
strict (every required field must be sent) with one argument: `partial=False` for PUT, `partial=True` for PATCH.

## Why Day 3 exists

Look at `create_movie`: we only check `title`. A wrong `genre`, a missing `imdb_code`, or a duplicate `imdb_code`
slip through, or crash with a database error (500). Writing an `if` for every rule, in every view, does not scale.
Tomorrow a **serializer** converts objects to JSON *and* validates input in one place.
