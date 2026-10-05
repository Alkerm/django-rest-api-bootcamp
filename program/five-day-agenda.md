# Five-Day Learning Agenda

**Building REST APIs with Django** · Tuwaiq Club at KFUPM · Modern Software & Cloud · **October 11-15, 2026**

> Source: *Task 02, Five-Day Learning Agenda* and *Estimated Daily Session Timing*, original PDFs in
> [`assets/source-documents/`](../assets/source-documents/).

## Program outcome

By the end of Day 5, participants can design, build, test, document, and deploy a database-backed REST API using
Django REST Framework, including token authentication, validated CRUD operations, and per-user permissions.

## The five-day journey

| Day | Date | Focus | Project increment | Daily proof |
|---|---|---|---|---|
| [1](../days/day-01/README.md) | Sun, Oct 11 | Foundations and setup | Repository, Django/DRF project, Task model, migrations, admin data | Server runs; Task records persist |
| [2](../days/day-02/README.md) | Mon, Oct 12 | Core API | Serializers, routes, and complete local CRUD endpoints | CRUD checklist passes |
| [3](../days/day-03/README.md) | Tue, Oct 13 | Realistic behaviour | Token auth, ownership, data isolation, permissions, validation | Two-user security check passes |
| [4](../days/day-04/README.md) | Wed, Oct 14 | Quality and delivery | Automated tests, README, environment and deployment configuration | Tests pass; fresh setup succeeds |
| [5](../days/day-05/README.md) | Thu, Oct 15 | Publish and demonstrate | Production deployment, smoke tests, final fixes, demonstration | Live URL and final evidence pass |

## Daily session timing (flexible 3-3.5 hours)

| Block | Duration |
|---|---|
| Explanation + demo | 45-60 min |
| Break / Q&A | 10 min |
| Practical application: exercise, then project milestone | 2-2.25 hours |

## Delivery model

**Per-day learning balance:** instructor explanation and demonstration ≈ **30%** of the session; at least **70%** is
guided exercises, project construction, troubleshooting, and practical verification.

**Facilitation rules**

- Use short explanations immediately followed by visible implementation.
- Keep one project repository growing across all five days.
- End each day with a practical exit check, not a knowledge-only quiz.
- Provide a known-good checkpoint so blocked participants can recover.
- Do not begin optional extensions until the day's required gate passes.

## How each day works in this repository

```text
Instructor explains + demos  →  days/day-0X/exercise/   →  days/day-0X/project-milestone.md  →  exit check
       (slides, example/)        practise on a Library API    apply it to YOUR Task API
```

## Day-by-day detail

### Day 1: Foundations, setup, and project start (Sunday, Oct 11)

- **Instructor explains:** the full request flow on the finished project; HTTP verbs on the Task resource; project vs
  app vs DRF; models, ORM, migrations; reproducibility (dependencies recorded, environments and secrets out of Git).
- **Instructor demonstrates:** virtual environment and dependency file; project + `tasks` app; DRF enabled; Task fields
  and status choices; owner → User; migrations; admin; a clean Day 1 commit.
- **Participants build:** the same, verifying folder structure, settings, migration output, and admin behaviour
  against the instructor reference at each checkpoint (in pairs).
- **Completion criteria:** a fresh terminal activates the environment and starts the server; `migrate` reports no
  pending migrations; Task fields and status choices match the scope; admin creates, updates, and persists Task
  records with owners; the repository is pushed with no secrets or environment folder.

### Day 2: Core API and complete CRUD (Monday, Oct 12)

- **Instructor explains:** the serializer as translator and gatekeeper; each operation's route, verb, success status
  and failure behaviour; viewsets and routers; one POST traced end to end; PUT vs PATCH.
- **Instructor demonstrates:** inspect a Task instance, serializer data and rendered JSON; `ModelSerializer` without an
  editable owner; a routed `ModelViewSet`; every endpoint in the browsable API or API client.
- **Participants build:** `TaskSerializer` (owner and generated fields read-only), `TaskViewSet` + router, session login
  as a development bridge, all six operations, valid/missing ids, database checks after each write.
- **Completion criteria:** routes resolve without manual URL duplication; create → 201 and the row exists; retrieve →
  200, unknown id → 404; PUT/PATCH change the intended fields; DELETE → 204; owner is read-only and server-assigned.

### Day 3: Authentication, ownership, and validation (Tuesday, Oct 13)

- **Instructor explains:** authentication vs authorization; tokens in the Authorization header; two users show why
  authentication alone is insufficient; defense in depth; validation as part of the contract; 401 vs 403 vs 404.
- **Instructor demonstrates:** `rest_framework.authtoken` and the token endpoint; two users' lists compared; the
  insecure base queryset, then filtered by `request.user`; read-only owner set in `perform_create`; field errors for
  blank title, invalid status, and past due date.
- **Participants build:** token support, tokens for two users, requests with and without the header, filtered
  querysets, automatic owner, blocked cross-user retrieve/update/delete, validation rules, the two-user scenario.
- **Completion criteria:** valid credentials return a token; no token → 401; client-supplied owner is ignored; each list
  contains only the caller's records; cross-user access is blocked without leaking data; blank title, invalid status,
  and past creation due date → 400.

### Day 4: Testing, quality, documentation, and delivery (Wednesday, Oct 14)

- **Instructor explains:** tests as executable promises; positive vs failure tests; test isolation; manual Day 3
  checks become automated; production configuration from environment variables; the README as part of the product.
- **Instructor demonstrates:** reusable test setup with two users and owned tasks; a 401 test and a cross-user test;
  reading a failing assertion and fixing the application; sensitive settings moved to environment variables; setup
  from README steps; deployment configuration walkthrough.
- **Participants build:** the first three tests with the instructor, then at least eight in total; repeated runs; README,
  dependencies, `.env.example`, production settings; repository exchange for a fresh-setup review; deployment rehearsal.
- **Completion criteria:** tests cover unauthenticated access, create/owner, own-only list, cross-user access, update,
  delete, validation; at least 8 pass with none skipped; fresh setup works without instructor correction; the README
  documents auth and every endpoint; production settings read from the environment; cloud accounts verified.

### Day 5: Deploy, verify, improve, and demonstrate (Thursday, Oct 15)

- **Instructor explains:** deployment as the same app under production configuration; the release sequence; log
  reading by failure category; smoke tests; technical demonstration; scope discipline.
- **Instructor demonstrates:** repository, service, database and variables connected; deployment and production
  migrations; a test user; one missing-variable or host error fixed from the logs; the required live flow.
- **Participants build:** deployment in small support groups using the runbook, recording evidence at each gate;
  troubleshooting; the production smoke test; final README; one small improvement only after the checklist passes;
  the live demo and submission.
- **Completion criteria:** public HTTPS URL reachable with current migrations; token auth and CRUD work in production;
  isolation and validation pass live; a record survives restart/redeploy; tests pass and the README is final; the
  submission is complete; the demo runs without instructor code changes.
