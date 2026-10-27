# Learning Outcomes

By the end of the program, participants can:

| # | Outcome | Taught on | Practised in | Verified by |
|---|---|---|---|---|
| 1 | Explain the client-server model, what a web framework does, and how HTTP methods, URLs, JSON, status codes, and request-response cycles work | Day 1-2 | every exercise | CRUD checklist (Day 2), submitted evidence |
| 2 | Explain tables, rows, keys and relationships, and model them with the Django ORM, migrations, and database-backed persistence | Day 1 | Day 1 exercise, Task model | Day 1 exit check |
| 3 | Build CRUD endpoints with function views (`@api_view`) and `path()` routing | Day 2 | Day 2 exercise, project | Day 2 exit check |
| 4 | Convert and validate data with serializers, with clear field-level errors | Day 3 | Day 3 exercise, project | Day 3 exit check |
| 5 | Apply token authentication and ownership rules in every view | Day 4 | Day 4 exercise, project | Day 4 two-user check |
| 6 | Configure, document, and verify an API (deployment: optional extension) | Day 4-5 | project | smoke test, README, submission |

## Daily learning outcomes

| Day | By the end of the session, participants can… |
|---|---|
| 1 | explain the basic HTTP request-response flow, run a reproducible Django REST Framework environment, and persist Task records through a correctly migrated data model. |
| 2 | write one function view per CRUD operation, connect each one to its own URL with `path()`, convert Task objects to JSON by hand, and return the right status code for every outcome. |
| 3 | replace hand-written conversion with a `ModelSerializer`, validate input and save data through it, tell PUT and PATCH apart, and reject invalid input with clear field-level errors. |
| 4 | secure the API with tokens, isolate each user's data in every view, and move configuration and secrets into environment variables. |
| 5 | verify the whole API with a smoke test, document it so a classmate can run it from a fresh clone, and submit the completed project with evidence. |

## Explicitly out of scope

- Frontend, mobile application, or visual dashboard
- Email verification, password reset, or social login
- Complex roles, teams, sharing, or notifications
- Microservices or production operations beyond one deployment
