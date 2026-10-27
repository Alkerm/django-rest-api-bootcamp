# Program Brief: Building REST APIs with Django

| Organization | Track | Program dates | Format |
|---|---|---|---|
| Tuwaiq Club at KFUPM | Modern Software & Cloud | October 25-29, 2026 | Five-day hands-on program |

> Source: *Task 01, Program Brief, Version 1.0 (Sep 27, 2026)*, original PDF in
> [`assets/source-documents/`](../assets/source-documents/). Scope changes after approval are recorded in a new
> document version.

## 1. Purpose and final outcome

**Purpose:** define the audience, learning scope, project requirements, daily milestones, and verifiable evidence of
success for a five-day Django REST API program.

**Final outcome:** by the end of Day 5, participants can **design, build, document, and verify a
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
project ends as a documented, verified service. **No frontend is required.**

Full requirements, API contract, Definition of Done and rubric: [`project/project-brief.md`](../project/project-brief.md).

## 5. Five connected daily milestones

Delivery baseline: five guided sessions of about three hours (~15 contact hours): about one hour of explanation, one
hour of exercise, and one hour of project work per day, plus optional homework.

> **Schedule change (Oct 27):** Monday's session (Oct 26) was cancelled because most participants had an exam. The
> remaining four days run as **two sessions of 8:00-10:00 PM**: Tuesday Oct 27 = Days 2 + 3, Wednesday Oct 28 =
> Days 4 + 5. The slides of both days are covered quickly, exercises are **optional**, and the time goes to the
> project. **Deployment is cancelled** (Oct 28); README and submission are due after Wednesday, and the submitted
> evidence replaces the live demonstration.

| Day | Date | Focus | Exit check |
|---|---|---|---|
| 1 | Oct 25 | Foundation | Repository is pushed. Server starts locally. Admin shows saved Task records after restart. |
| 2 | Oct 27 (with Day 3) | Core API: CRUD with function views | All CRUD operations work locally with valid JSON and appropriate status codes. A blank title is rejected. |
| 3 | Oct 27 (with Day 2) | Serialization and validation | Every view uses the serializer. Invalid data is rejected with field-level errors. |
| 4 | Oct 28 (with Day 5) | Security and configuration | User A cannot view or modify User B's tasks. Requests without a token get 401. Settings come from the environment. |
| 5 | Oct 28 (with Day 4) | Finish and submit | The smoke test passes locally, a fresh clone can be set up from the README, and all required evidence is submitted (by the announced deadline). |

Detailed daily plan: [`five-day-agenda.md`](five-day-agenda.md).

## 6. Pacing and delivery safeguards

- The instructor maintains a known-good **checkpoint** for the start of each day
  ([`project/checkpoints/`](../project/checkpoints/)).
- Participants who miss an exit check start the next session from the checkpoint, preserving Day 5 completion.
- Deployment (Render + Neon) was cancelled for this cohort; `setup/deployment.md` remains as an optional extension.
- Stretch features are taught only after the minimum project works and the day's exit check passes.

## 7. Final evidence of completion

**Submission package**

- GitHub repository URL accessible to reviewers
- README with setup, usage, endpoint, and smoke-test instructions
- Smoke-test output against the local server (10/10)
- No exposed credentials or secrets

**Required evidence flow** (shown live in earlier plans; this cohort shows it through the README and the submission)

- Obtain a token and authenticate
- Create and list personal tasks
- Update one task and show a validation failure
- Prove cross-user data isolation
- Delete a task and confirm the live service persists data

## 8. Definition of done and assessment

See [`project/project-brief.md`](../project/project-brief.md#definition-of-done).
