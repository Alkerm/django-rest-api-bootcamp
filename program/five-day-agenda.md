# Five-Day Learning Agenda

**Building REST APIs with Django** · Tuwaiq Club at KFUPM · Modern Software & Cloud · **October 11-15, 2026**

> Based on *Task 02, Five-Day Learning Agenda* and *Estimated Daily Session Timing* (original PDFs in
> [`assets/source-documents/`](../assets/source-documents/)), **rebalanced for a 1 h + 1 h + 1 h day**: validation
> moved from Day 3 to Day 2, the README moved from Day 4 to Day 5, and Day 5's middle hour is a guided deployment.
> The final outcome is unchanged.

## Program outcome

By the end of Day 5, participants can design, build, test, document, and deploy a database-backed REST API using
Django REST Framework, including token authentication, validated CRUD operations, and per-user permissions.

## The five-day journey

| Day | Date | Focus | Project increment | Daily proof |
|---|---|---|---|---|
| [1](../days/day-01/README.md) | Sun, Oct 11 | Foundations and setup | Repository, Django/DRF project, Task model, migrations, admin data | Server runs; Task records persist |
| [2](../days/day-02/README.md) | Mon, Oct 12 | Core API: CRUD + validation | Serializer, routes, complete CRUD endpoints, validation rules | CRUD checklist passes; invalid input → 400 |
| [3](../days/day-03/README.md) | Tue, Oct 13 | Security | Token auth, ownership, data isolation, permissions | Two-user security check passes |
| [4](../days/day-04/README.md) | Wed, Oct 14 | Testing and configuration | Automated tests, settings from the environment, deployment packages | 8 required tests pass |
| [5](../days/day-05/README.md) | Thu, Oct 15 | Publish and demonstrate | Production deployment, smoke test, final README, demonstration | Live URL and final evidence pass |

## Daily session timing (about 3 hours)

| Block | Duration | Days 1-4 | Day 5 |
|---|---|---|---|
| 1. Explanation + live demo | ~60 min | instructor | instructor (includes a live deployment) |
| 2. Practice | ~60 min | **exercise** (Library API, core tasks first) | **guided deployment** of each participant's project |
| 3. Project | ~60 min | **project milestone** (Task API) | verify, README, submit, live demo |

Short breaks between blocks. Every exercise marks tasks as **core** or **stretch**; the project milestone is what is
assessed, so stretch tasks never block anyone.

## Delivery model

**Per-day learning balance:** instructor explanation and demonstration ≈ **one third** of the session; two thirds are
hands-on: the exercise, then the project milestone.

**Facilitation rules**

- Use short explanations immediately followed by visible implementation.
- Keep one project repository growing across all five days.
- End each day with a practical exit check, not a knowledge-only quiz.
- Provide a known-good checkpoint so blocked participants can recover.
- Do not begin optional extensions until the day's required gate passes.

## How each day works in this repository

```text
Instructor explains + demos  →  days/day-0X/exercise/   →  days/day-0X/project-milestone.md  →  exit check
   (~60 min: slides, example/)   (~60 min: Library API)       (~60 min: YOUR Task API)
```

## Day-by-day detail

### Day 1: Foundations, setup, and project start (Sunday, Oct 11)

- **Instructor explains (~60 min):** the full request flow on the finished project; HTTP verbs on the Task resource;
  project vs app vs DRF; a live model → migration → admin → ORM demo; reproducibility (dependencies recorded,
  environments and secrets out of Git).
- **Exercise (~60 min):** Library catalog: `Book` model, migrations, sample data, admin (+ ORM practice as stretch).
- **Project (~60 min):** copy the starter, Task fields and status choices, owner → User, migrations, admin, two users,
  first GitHub push. If the push runs over, it finishes in the first 10 minutes of Day 2.
- **Completion criteria:** a fresh terminal activates the environment and starts the server; `migrate` reports no
  pending migrations; Task fields and status choices match the scope; admin creates, updates, and persists Task
  records with owners; the repository is pushed with no secrets or environment folder.

### Day 2: Core API, CRUD and validation (Monday, Oct 12)

- **Instructor explains (~60 min):** the serializer as translator and gatekeeper; viewsets and routers; the CRUD
  contract and status codes; one POST traced end to end; PUT vs PATCH; validation: built-in rules, clearer messages
  with `extra_kwargs`, `validate_<field>`, and `self.instance` (create vs update).
- **Exercise (~60 min):** Book CRUD API: serializer, viewset, router, two validation rules (+ ordering and a CRUD
  checklist as stretch).
- **Project (~60 min):** `TaskSerializer` (owner and generated fields read-only), `TaskViewSet` + router, session login
  as a development bridge, all six operations, title error messages, due date not in the past on create.
- **Completion criteria:** routes resolve without manual URL duplication; create → 201 and the row exists; retrieve →
  200, unknown id → 404; PUT/PATCH change the intended fields; DELETE → 204; owner is read-only and server-assigned;
  blank title, invalid status, and a past creation due date → 400 with field errors.

### Day 3: Authentication, ownership, and permissions (Tuesday, Oct 13)

- **Instructor explains (~60 min):** authentication vs authorization; tokens in the Authorization header; Postman with
  a token; two users show why authentication alone is insufficient (attack-and-fix demo); filtering by `request.user`;
  defense in depth; 401 vs 403 vs 404.
- **Exercise (~60 min):** personal reading list: token login, `get_queryset` + `perform_create` (+ user-aware validation
  as stretch).
- **Project (~60 min):** token support, token endpoint, filtered querysets, automatic owner, the 8-step two-user
  scenario (+ `IsOwner` and owner shown as username as stretch).
- **Completion criteria:** valid credentials return a token; no token → 401; a client-supplied owner is ignored; each
  list contains only the caller's records; cross-user access is blocked (404) without leaking data.

### Day 4: Testing and configuration (Wednesday, Oct 14)

- **Instructor explains (~60 min):** tests as executable promises; positive vs failure tests; test isolation;
  `APITestCase`, `setUp` and tokens in tests; reading a failing assertion and fixing the application; configuration
  from environment variables, `.env.example`, deployment packages.
- **Exercise (~60 min):** 4 required tests for the reading-list API (+4 tests and a "break it on purpose" experiment as
  stretch).
- **Project (~60 min):** the example + 7 required tests (8 in total, two built with the instructor), settings from the
  environment, `.env.example`, deployment packages in `requirements.txt` (+7 stretch tests).
- **Optional homework (~15 min):** open the Neon and Render accounts and read the deployment guide.
- **Completion criteria:** tests cover unauthenticated access, create/owner, own-only list, cross-user access, update,
  delete, validation; at least 8 pass with none of the required ones skipped; production settings read from the
  environment; `pip check` is clean.

### Day 5: Deploy, verify, and demonstrate (Thursday, Oct 15)

- **Instructor explains (~60 min):** deployment as the same app under production configuration; a live deployment of
  the reference project; log reading by failure category; smoke tests and persistence; the 5-minute demo.
- **Guided deployment (~60 min, replaces the exercise):** the `DATABASE_URL` setting (WhiteNoise, static files and CSRF
  origins come pre-written), Neon database, Render web service, environment variables, production users, everyone
  step by step with the instructor.
- **Project (~60 min):** smoke test against the live URL, persistence check, complete README, submission, and the live
  demo at one of 2-3 parallel review stations as soon as each participant is ready.
- **Completion criteria:** public HTTPS URL reachable with current migrations; token auth and CRUD work in production;
  isolation and validation pass live; a record survives restart/redeploy; tests pass; the README lets a new reviewer
  set the project up from a fresh clone; the submission is complete; the demo runs without instructor code changes.
