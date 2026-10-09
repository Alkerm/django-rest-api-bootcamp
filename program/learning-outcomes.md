# Learning Outcomes

By the end of the program, participants can:

| # | Outcome | Taught on | Practised in | Verified by |
|---|---|---|---|---|
| 1 | Explain how HTTP methods, URLs, JSON, status codes, and request-response cycles work | Day 1-2 | every exercise | CRUD checklist (Day 2), live demo |
| 2 | Model relational data with the Django ORM, migrations, and database-backed persistence | Day 1 | Day 1 exercise, Task model | Day 1 exit check |
| 3 | Build serializers, views/viewsets, routes, and validated CRUD endpoints with Django REST Framework | Day 2 | Day 2 exercise, project | Day 2 exit check |
| 4 | Apply token authentication, ownership rules, and object permissions | Day 3 | Day 3 exercise, project | Day 3 two-user check |
| 5 | Write automated API tests and diagnose failures using clear test feedback | Day 4 | Day 4 exercise, project | ≥ 8 passing tests |
| 6 | Configure, document, deploy, and verify an API in a production environment | Day 4-5 | Day 5 exercise, project | live HTTPS URL, smoke test, demo |

## Daily learning outcomes

| Day | By the end of the session, participants can… |
|---|---|
| 1 | explain the basic HTTP request-response flow, run a reproducible Django REST Framework environment, and persist Task records through a correctly migrated data model. |
| 2 | convert Task objects to validated JSON, implement routed create, list, retrieve, update, partial-update, and delete operations, and reject invalid input with clear field-level errors. |
| 3 | secure the API with tokens, isolate each user's data, and enforce ownership at query and object level. |
| 4 | verify API behavior with automated tests, read a failing test to find a bug, and move configuration and secrets into environment variables. |
| 5 | release the API to a public HTTPS environment, verify production behavior and persistence, correct deployment issues, and demonstrate the completed system with evidence. |

## Explicitly out of scope

- Frontend, mobile application, or visual dashboard
- Email verification, password reset, or social login
- Complex roles, teams, sharing, or notifications
- Microservices or production operations beyond one deployment
