# Day 2 Worked Example: Movies API

Read-only example files (Movies domain, models from [`../../day-01/example/models.py`](../../day-01/example/models.py)).

| File | Shows |
|---|---|
| [`serializers.py`](serializers.py) | `ModelSerializer`, `fields`, `read_only_fields`, a read-only related field with `source=` |
| [`views.py`](views.py) | `ModelViewSet` vs `ReadOnlyModelViewSet`, `perform_create` |
| [`urls.py`](urls.py) | `DefaultRouter`, the generated URLs and their names |

## One POST request, step by step

```text
POST /api/movies/  {"title": "Dune", "imdb_code": "tt1160419", "director": 1}
  │
  ├─ router          → MovieViewSet.create
  ├─ serializer      → is_valid()?  no → 400 + {"field": ["error"]}       (nothing saved)
  │                                 yes ↓
  ├─ perform_create  → serializer.save(added_by=request.user)  → INSERT row
  └─ response        → 201 Created + the new movie as JSON (including id and created_at)
```

## The CRUD contract

| Action | Method + URL | Success | Typical failures |
|---|---|---|---|
| list | `GET /api/movies/` | 200 + array | none |
| create | `POST /api/movies/` | 201 + object | 400 invalid body |
| retrieve | `GET /api/movies/{id}/` | 200 + object | 404 unknown id |
| update | `PUT /api/movies/{id}/` | 200 + object | 400 (all required fields must be sent), 404 |
| partial_update | `PATCH /api/movies/{id}/` | 200 + object | 400, 404 |
| destroy | `DELETE /api/movies/{id}/` | 204, empty body | 404 |

## PUT vs PATCH

Stored movie: `{"title": "Dune", "genre": "DRAMA", "imdb_code": "tt1160419", "director": 1}`

| Request | Result |
|---|---|
| `PATCH {"genre": "COMEDY"}` | 200: only `genre` changes |
| `PUT {"genre": "COMEDY"}` | **400**: `title`, `imdb_code`, `director` are required, because PUT means "here is the whole new object" |
| `PUT {"title": "Dune", "genre": "COMEDY", "imdb_code": "tt1160419", "director": 1}` | 200 |
