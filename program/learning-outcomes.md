# Learning Outcomes

By the end of the program, participants can:

| # | Outcome | Taught on | Practised in | Verified by |
|---|---|---|---|---|
| 1 | Explain how HTTP methods, URLs, JSON, status codes, and request-response cycles work | Day 1-2 | every exercise | CRUD checklist (Day 2), live demo |
| 2 | Model relational data with the Django ORM, migrations, and database-backed persistence | Day 1 | Day 1 exercise, Task model | Day 1 exit check |
| 3 | Build serializers, views/viewsets, routes, and CRUD endpoints with Django REST Framework | Day 2 | Day 2 exercise, project | Day 2 exit check |
| 4 | Apply token authentication, ownership rules, object permissions, and input validation | Day 3 | Day 3 exercise, project | Day 3 two-user check |
| 5 | Write automated API tests and diagnose failures using clear test feedback | Day 4 | Day 4 exercise, project | ≥ 8 passing tests |
| 6 | Configure, document, deploy, and verify an API in a production environment | Day 4-5 | Day 5 exercise, project | live HTTPS URL, smoke test, demo |

## Daily learning outcomes

| Day | By the end of the session, participants can… |
|---|---|
| 1 | explain the basic HTTP request-response flow, run a reproducible Django REST Framework environment, and persist Task records through a correctly migrated data model. |
| 2 | convert Task objects to validated JSON and implement routed create, list, retrieve, update, partial-update, and delete operations with appropriate HTTP responses. |
| 3 | secure the API with tokens, isolate each user's data, enforce ownership at query and object level, and return clear validation errors for realistic invalid input. |
| 4 | verify API behaviour with automated tests, document a reproducible setup, protect configuration secrets, and complete a deployment rehearsal with production-ready settings. |
| 5 | release the API to a public HTTPS environment, verify production behaviour and persistence, correct deployment issues, and demonstrate the completed system with evidence. |

## Explicitly out of scope

- Frontend, mobile application, or visual dashboard
- Email verification, password reset, or social login
- Complex roles, teams, sharing, or notifications
- Microservices or production operations beyond one deployment
