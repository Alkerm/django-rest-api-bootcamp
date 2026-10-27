# Project Brief: Personal Task Management REST API

Each participant builds **one** API, in their **own** GitHub repository, through five connected daily increments.
Authenticated users create and manage **only their own** tasks. The API validates input and prevents access to other
users' data. It ends as a documented, verified service. No frontend is required.

## How the project folders work

| Folder | What it is | When to use it |
|---|---|---|
| [`starter/`](starter/) | the Day 1 starting point: a generated Django project with Day 1 TODOs | copy it once on Day 1 into your own `task-management-api` folder |
| [`checkpoints/day-02`](checkpoints/day-02) … [`day-04`](checkpoints/day-04) | the start of each day: **all previous days solved** + that day's TODOs (`day-04` is final: it also holds the Day 5 TODOs) | copy the whole folder over your project at the start of Days 2, 3 and 4; nothing to copy on Day 5 |
| [`reference-solution/`](reference-solution/) | the complete project (instructor repository) | after the program |

Every TODO looks like this and points to a hint:

```python
# TODO [Day 4 · P4]: Replace "all tasks" with "only my tasks" (owner = request.user).
#   ...exact rules and names...
# HINT: days/day-04/hints.md#p4  |  Example: days/day-04/example/views.py
# YOUR CODE HERE
```

## Minimum project requirements

| Area | Required for completion | Acceptance check |
|---|---|---|
| Data model | Task fields: `id`, `title`, `description`, `status`, `due_date`, `owner`, `created_at`, `updated_at`. Status choices: `TODO`, `IN_PROGRESS`, `DONE`. | Migrations apply successfully and data persists after a server restart. |
| CRUD API | Authenticated users can create, list, retrieve, fully/partially update, and delete tasks. | Every operation returns an appropriate JSON response and HTTP status code. |
| Authentication | DRF token authentication. Tokens are issued through a login endpoint. Test users may be created through Django admin or a documented command. | Protected task endpoints reject unauthenticated requests with **401**. |
| Ownership | The API assigns `owner` from the authenticated user. Users can list, retrieve, update, and delete only their own tasks. | A second user cannot view or modify the first user's tasks (**404**). |
| Validation | Title is required and nonblank; status must use an allowed value; due date cannot be earlier than today when a task is created; owner is read-only. | Invalid input returns **400** with clear field-level error messages. |
| Documentation | README includes setup, environment variables, migrations, authentication, endpoint examples, the smoke-test command, and project decisions. | A new reviewer can run and use the project from the README. |
| Source control | GitHub repository visible to reviewers, meaningful commit history, dependency file, sample environment file, and no committed secrets. | Repository can be cloned; `.env` is ignored; setup is reproducible. |

## Required API contract

| Method | Path | Purpose | Auth | Success |
|---|---|---|---|---|
| POST | `/api/auth/token/` | Exchange a valid username/password for an API token | No | 200 |
| GET | `/api/tasks/` | List only the authenticated user's tasks | Yes | 200 |
| POST | `/api/tasks/create/` | Create a task owned by the authenticated user | Yes | 201 |
| GET | `/api/tasks/{id}/` | Retrieve one owned task | Yes | 200 |
| PUT / PATCH | `/api/tasks/{id}/update/` | Replace or partially update one owned task | Yes | 200 |
| DELETE | `/api/tasks/{id}/delete/` | Delete one owned task | Yes | 204 |

Each operation is one **function view** (`@api_view`) on its own URL, connected with `path()`. A wrong method on a URL
(for example `DELETE /api/tasks/{id}/`) returns `405`.

**Agreed error behavior:** no or invalid token → `401` · another user's task → `404` (it is invisible, so its
existence is not revealed) · invalid input → `400` with `{"field": ["message"]}`.

## Daily increments

| Day | Increment | Milestone page | Start folder |
|---|---|---|---|
| 1 | repository, project, `Task` model, migrations, admin data | [day-01](../days/day-01/project-milestone.md) | `starter/` |
| 2 | CRUD with five function views and `path()` routes (objects converted by hand) | [day-02](../days/day-02/project-milestone.md) | `checkpoints/day-02` |
| 3 | `TaskSerializer` in every view, validation rules | [day-03](../days/day-03/project-milestone.md) | `checkpoints/day-03` |
| 4 | token auth, ownership in every view, env configuration | [day-04](../days/day-04/project-milestone.md) | `checkpoints/day-04` |
| 5 | smoke test, final README, submission (deployment cancelled for this cohort) | [day-05](../days/day-05/project-milestone.md) | keep working in your project (TODOs came with `day-04`) |

<a id="optional-extensions"></a>
## Optional extensions and out of scope

| Optional extensions (only after every requirement passes) | Explicitly out of scope |
|---|---|
| Filtering, search, ordering, or pagination | Frontend, mobile application, or visual dashboard |
| Priority, tags, categories, or completion statistics | Email verification, password reset, or social login |
| JWT authentication or user registration | Complex roles, teams, sharing, or notifications |
| Deployment to Render + Neon ([`setup/deployment.md`](../setup/deployment.md)) | |
| OpenAPI documentation and Swagger UI | Microservices or production operations beyond one deployment |
| Automated tests (`APITestCase`), CI, Docker, or throttling | Optional items as conditions for passing |

**Scope rule:** optional work begins only after all minimum requirements pass locally. Optional features never block
program completion.

<a id="definition-of-done"></a>
## Definition of Done: every item must pass

- [ ] All required Task fields and CRUD endpoints are implemented.
- [ ] Protected endpoints require authentication and enforce per-user ownership.
- [ ] Required validation returns correct error responses.
- [ ] The repository is reproducible, documented, and free of committed secrets.
- [ ] The smoke test passes against the participant's local server (10/10).
- [ ] A reviewer can set the project up from the README and see the required flow working (this cohort: no live demo).

## Assessment rubric

| Assessment area | Weight | Pass standard |
|---|---|---|
| Core API and data model | 25% | Required fields, persistence, and complete CRUD behavior |
| Authentication and ownership | 35% | Protected endpoints and a successful cross-user isolation check |
| Validation and API behavior | 20% | Required rules, clear errors, and appropriate status codes |
| Documentation and repository | 20% | Reproducible setup, useful README, passing smoke test, clean Git history, no secrets |

**Passing rule:** every Definition of Done item is mandatory. The rubric supports consistent feedback; it does not
allow a participant to compensate for a missing mandatory item with optional features.

## Submission package

Submitted after the last session (Wednesday, Oct 28) through the [submission form](https://forms.gle/SjbXGzfP1zYCdjfN8), by the
deadline the instructors announce.

- GitHub repository URL accessible to reviewers
- README with setup, usage, endpoint, and smoke-test instructions
- Smoke-test output against the local server (10/10)
- No exposed credentials or secrets
