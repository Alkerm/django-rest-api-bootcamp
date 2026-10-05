# Program Brief: Building REST APIs with Django

| Organization | Track | Program dates | Format |
|---|---|---|---|
| Tuwaiq Club at KFUPM | Modern Software & Cloud | October 11-15, 2026 | Five-day hands-on program |

> Source: *Task 01, Program Brief, Version 1.0 (Sep 27, 2026)*, original PDF in
> [`assets/source-documents/`](../assets/source-documents/). Scope changes after approval are recorded in a new
> document version.

## 1. Purpose and final outcome

**Purpose:** define the audience, learning scope, project requirements, daily milestones, and verifiable evidence of
success for a five-day Django REST API program.

**Final outcome:** by the end of Day 5, participants can **design, build, test, document, and deploy a
database-backed REST API using Django REST Framework**, including authentication, validated CRUD operations, and
per-user permissions.

## 2. Audience and entry requirements

**Who it is for:** KFUPM university students and beginner developers who can write small Python programs and want
practical backend development experience. Prior experience with Django, REST APIs, databases, or cloud deployment is
**not** required.

**Required before Day 1** (details in [`setup/prerequisites.md`](../setup/prerequisites.md)):

- Python variables, functions, conditionals, loops, lists, and dictionaries
- Basic classes, objects, and exception handling
- Terminal navigation plus pip and virtual environments
- Basic Git/GitHub: clone, add, commit, push, and pull
- A laptop with Python, Git, a code editor, and a GitHub account

## 3. What participants will learn

See [`learning-outcomes.md`](learning-outcomes.md).

## 4. Practical project: Personal Task Management REST API

Starting on Day 1, each participant builds **one** API through five connected increments. Authenticated users can
create and manage their own tasks while the system validates input and prevents access to other users' data. The
project ends as a tested, documented, deployed service. **No frontend is required.**

Full requirements, API contract, Definition of Done and rubric: [`project/project-brief.md`](../project/project-brief.md).

## 5. Five connected daily milestones

Delivery baseline: five guided sessions of about three hours (~15 contact hours), supported by up to one hour of
optional independent work per day.

| Day | Date | Focus | Exit check |
|---|---|---|---|
| 1 | Oct 11 | Foundation | Repository is pushed. Server starts locally. Admin shows saved Task records after restart. |
| 2 | Oct 12 | Core API | All CRUD operations work locally with valid JSON and appropriate status codes. |
| 3 | Oct 13 | Security | User A cannot view or modify User B's tasks. Invalid data is rejected with field-level errors. |
| 4 | Oct 14 | Quality and delivery | All tests pass. A fresh clone can be set up from the README. Deployment configuration is ready. |
| 5 | Oct 15 | Publish and demonstrate | Public HTTPS URL works, data persists, all required evidence is submitted, and the live demo passes. |

Detailed daily plan: [`five-day-agenda.md`](five-day-agenda.md).

## 6. Pacing and delivery safeguards

- The instructor maintains a known-good **checkpoint** for the start of each day
  ([`project/checkpoints/`](../project/checkpoints/)).
- Participants who miss an exit check start the next session from the checkpoint, preserving Day 5 completion.
- Cloud accounts and the approved platform are verified before Day 4. Deployment is rehearsed on Day 4, not left
  entirely to Day 5.
- Stretch features are taught only after the minimum project works and all required tests pass.

## 7. Final evidence of completion

**Submission package**

- GitHub repository URL accessible to reviewers
- Public HTTPS deployment URL
- README with setup, usage, endpoint, test, and deployment instructions
- Passing automated test output for at least 8 tests
- No exposed credentials or secrets

**Required live demonstration**

- Obtain a token and authenticate
- Create and list personal tasks
- Update one task and show a validation failure
- Prove cross-user data isolation
- Delete a task and confirm the live service persists data

## 8. Definition of done and assessment

See [`project/project-brief.md`](../project/project-brief.md#definition-of-done).
