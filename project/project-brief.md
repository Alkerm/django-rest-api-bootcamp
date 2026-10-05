# Project Brief: Personal Task Management REST API

Each participant builds **one** API, in their **own** GitHub repository, through five connected daily increments.
Authenticated users create and manage **only their own** tasks. The API validates input and prevents access to other
users' data. It ends as a tested, documented, deployed service. No frontend is required.

## How the project folders work

| Folder | What it is | When to use it |
|---|---|---|
| [`starter/`](starter/) | the Day 1 starting point: a generated Django project with Day 1 TODOs | copy it once on Day 1 into your own `task-management-api` folder |
| [`checkpoints/day-02`](checkpoints/day-02) … [`day-05`](checkpoints/day-05) | the start of each day: **all previous days solved** + that day's TODOs | copy the new files from it each morning, or the whole folder if you fell behind |
| [`reference-solution/`](reference-solution/) | the complete project (instructor repository) | after the program |

Every TODO looks like this and points to a hint:

```python
# TODO [Day 3 · P4]: Replace "all tasks" with "only my tasks".
#   ...exact rules and names...
# HINT: days/day-03/hints.md#p4  |  Example: days/day-03/example/views.py
# YOUR CODE HERE
```

## Minimum project requirements

| Area | Required for completion | Acceptance check |
|---|---|---|
| Data model | Task fields: `id`, `title`, `description`, `status`, `due_date`, `owner`, `created_at`, `updated_at`. Status choices: `TODO`, `IN_PROGRESS`, `DONE`. | Migrations apply successfully and data persists after restart/redeploy. |
| CRUD API | Authenticated users can create, list, retrieve, fully/partially update, and delete tasks. | Every operation returns an appropriate JSON response and HTTP status code. |
| Authentication | DRF token authentication. Tokens are issued through a login endpoint. Test users may be created through Django admin or a documented command. | Protected task endpoints reject unauthenticated requests with **401**. |
| Ownership | The API assigns `owner` from the authenticated user. Users can list, retrieve, update, and delete only their own tasks. | A second user cannot view or modify the first user's tasks (**404**). |
| Validation | Title is required and nonblank; status must use an allowed value; due date cannot be earlier than today when a task is created; owner is read-only. | Invalid input returns **400** with clear field-level error messages. |
| Testing | At least 8 automated tests using DRF `APITestCase` or equivalent, covering authentication, CRUD, ownership/data isolation, and validation. | The documented test command completes with all tests passing. |
| Documentation | README includes setup, environment variables, migrations, test command, authentication, endpoint examples, deployed URL, and project decisions. | A new reviewer can run and use the project from the README. |
| Deployment | Public HTTPS deployment on the program-approved platform (Render + Neon PostgreSQL), with production settings and a persistent database. | The live URL supports the required demonstration flow and retains data. |
| Source control | GitHub repository visible to reviewers, meaningful commit history, dependency file, sample environment file, and no committed secrets. | Repository can be cloned; `.env` is ignored; setup is reproducible. |

## Required API contract

| Method | Path | Purpose | Auth | Success |
|---|---|---|---|---|
| POST | `/api/auth/token/` | Exchange a valid username/password for an API token | No | 200 |
| GET | `/api/tasks/` | List only the authenticated user's tasks | Yes | 200 |
| POST | `/api/tasks/` | Create a task owned by the authenticated user | Yes | 201 |
| GET | `/api/tasks/{id}/` | Retrieve one owned task | Yes | 200 |
| PUT / PATCH | `/api/tasks/{id}/` | Replace or partially update one owned task | Yes | 200 |
| DELETE | `/api/tasks/{id}/` | Delete one owned task | Yes | 204 |

**Agreed error behaviour:** no or invalid token → `401` · another user's task → `404` (it is invisible, so its
existence is not revealed) · invalid input → `400` with `{"field": ["message"]}`.

## Daily increments

| Day | Increment | Milestone page | Start folder |
|---|---|---|---|
| 1 | repository, project, `Task` model, migrations, admin data | [day-01](../days/day-01/project-milestone.md) | `starter/` |
| 2 | serializer, viewset, router, CRUD | [day-02](../days/day-02/project-milestone.md) | `checkpoints/day-02` |
| 3 | token auth, ownership, permissions, validation | [day-03](../days/day-03/project-milestone.md) | `checkpoints/day-03` |
| 4 | tests, README, env configuration, deploy rehearsal | [day-04](../days/day-04/project-milestone.md) | `checkpoints/day-04` |
| 5 | production settings, deployment, smoke test, demo | [day-05](../days/day-05/project-milestone.md) | `checkpoints/day-05` |

<a id="optional-extensions"></a>
## Optional extensions and out of scope

| Optional extensions (only after every requirement passes) | Explicitly out of scope |
|---|---|
| Filtering, search, ordering, or pagination | Frontend, mobile application, or visual dashboard |
| Priority, tags, categories, or completion statistics | Email verification, password reset, or social login |
| JWT authentication or user registration | Complex roles, teams, sharing, or notifications |
| OpenAPI documentation and Swagger UI | Microservices or production operations beyond one deployment |
| CI, Docker, throttling, or expanded test coverage | Optional items as conditions for passing |

**Scope rule:** optional work begins only after all minimum requirements pass locally. Optional features never block
program completion.

<a id="definition-of-done"></a>
## Definition of Done: every item must pass

- [ ] All required Task fields and CRUD endpoints are implemented.
- [ ] Protected endpoints require authentication and enforce per-user ownership.
- [ ] Required validation returns correct error responses.
- [ ] At least 8 automated tests pass with no required tests skipped.
- [ ] The repository is reproducible, documented, and free of committed secrets.
- [ ] The deployed API is publicly reachable over HTTPS and uses persistent storage.
- [ ] The participant completes the required live demonstration without instructor code changes.

## Assessment rubric

| Assessment area | Weight | Pass standard |
|---|---|---|
| Core API and data model | 25% | Required fields, persistence, and complete CRUD behaviour |
| Authentication and ownership | 25% | Protected endpoints and a successful cross-user isolation check |
| Validation and API behaviour | 15% | Required rules, clear errors, and appropriate status codes |
| Automated tests | 15% | At least 8 meaningful tests; all required tests pass |
| Documentation and repository | 10% | Reproducible setup, useful README, clean Git history, no secrets |
| Deployment and demonstration | 10% | Working HTTPS deployment and complete live demonstration |

**Passing rule:** every Definition of Done item is mandatory. The rubric supports consistent feedback; it does not
allow a participant to compensate for a missing mandatory item with optional features.

## Submission package

- GitHub repository URL accessible to reviewers
- Public HTTPS deployment URL
- README with setup, usage, endpoint, test, and deployment instructions
- Passing automated test output for at least 8 tests
- No exposed credentials or secrets
