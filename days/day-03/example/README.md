# Day 3 Worked Example: Movies API with a Serializer

Read-only example files (Movies domain, models from [`../../day-01/example/models.py`](../../day-01/example/models.py),
URLs unchanged from [`../../day-02/example/urls.py`](../../day-02/example/urls.py)).

| File | Shows |
|---|---|
| [`serializers.py`](serializers.py) | `ModelSerializer`, `fields`, `read_only_fields`, a read-only related field with `source=`, the three validation levels: `extra_kwargs` messages, `validate_<field>` (with `self.instance`), `validate(attrs)` |
| [`views.py`](views.py) | Day 2's five function views rewritten with the serializer: `many=True`, `data=`, `is_valid()`, `serializer.errors`, `save()`, `partial=` |

## Day 2 vs Day 3

| Job | Day 2 (by hand) | Day 3 (serializer) |
|---|---|---|
| object → JSON | `movie_to_dict(movie)` | `MovieSerializer(movie).data` |
| many objects → JSON | `[movie_to_dict(m) for m in movies]` | `MovieSerializer(movies, many=True).data` |
| check the input | one `if` per rule, in every view | `serializer.is_valid()`: every rule, declared once |
| error format | built by hand | `serializer.errors` → `{"field": ["message"]}` |
| save | `Movie.objects.create(title=..., genre=..., ...)` | `serializer.save(added_by=request.user)` |
| PUT vs PATCH | same code for both | `partial=False` (PUT: all fields required) / `partial=True` (PATCH) |

## One POST request, step by step

```text
POST /api/movies/create/  {"title": "Dune", "imdb_code": "tt1160419", "director": 1}
  │
  ├─ urls.py         → create_movie(request)
  ├─ serializer      → is_valid()?  runs built-in rules → validate_<field> → validate(attrs)
  │                    no → 400 + serializer.errors      (nothing saved)
  │                    yes ↓
  ├─ save()          → serializer.save(added_by=request.user)  → INSERT row
  └─ Response        → 201 Created + serializer.data (including id, director_name and created_at)
```

## Three levels of validation

| Level | Where | Example | Error appears under |
|---|---|---|---|
| 1. Built-in | the model field (no code) | `title` missing, `genre` not a choice, duplicate `imdb_code`, unknown `director` id | the field name |
| 1b. Custom text for a built-in rule | `extra_kwargs` in `Meta` | `"Title cannot be blank."` | the field name |
| 2. Field-level | `def validate_release_date(self, value)` | no future release date (on create only: `self.instance is None`) | `release_date` |
| 3. Object-level | `def validate(self, attrs)` | a documentary needs a release date | `non_field_errors` |

## PUT vs PATCH

Stored movie: `{"title": "Dune", "genre": "DRAMA", "imdb_code": "tt1160419", "director": 1}`

| Request | Result |
|---|---|
| `PATCH {"genre": "COMEDY"}` | 200: only `genre` changes |
| `PUT {"genre": "COMEDY"}` | **400**: `title`, `imdb_code`, `director` are required, because PUT means "here is the whole new object" |
| `PUT {"title": "Dune", "genre": "COMEDY", "imdb_code": "tt1160419", "director": 1}` | 200 |
