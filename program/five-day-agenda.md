# Five-Day Learning Agenda

**Building REST APIs with Django** · Tuwaiq Club at KFUPM · Modern Software & Cloud · **October 25-29, 2026**

> Based on *Task 02, Five-Day Learning Agenda* and *Estimated Daily Session Timing* (original PDFs in
> [`assets/source-documents/`](../assets/source-documents/)), **rebalanced for a 1 h + 1 h + 1 h day**: validation
> moved from Day 3 to Day 2, the README moved from Day 4 to Day 5, and Day 5's middle hour is a guided deployment.
> The final outcome is unchanged. Approval copy: [`02-five-day-agenda-v2.pdf`](../assets/source-documents/02-five-day-agenda-v2.pdf).
>
> **Restructured on Oct 23, 2026** (supersedes the PDF where they differ): Day 1 adds client/server, an HTTP
> request/response example, "what is a web framework" and more time on databases; Day 2 builds CRUD with one
> function view per operation and `path()` routing (no serializers); Day 3 is serialization + validation; Day 4 is
> security (moved from Day 3) + configuration; automated testing is no longer taught.
>
> **Schedule change on Oct 27:** Monday's session was cancelled (participants' exam). Days 2-5 run as two
> sessions, **8:00-10:00 PM**: **Tue Oct 27 = Days 2 + 3**, **Wed Oct 28 = Days 4 + 5**. The instructor covers
> both days' slides quickly and may solve some exercise tasks live; exercises are optional; the rest of the time
> is project work. Deployment happens on Wednesday; README + submission are due afterwards; no live demo.

## Program outcome

By the end of Day 5, participants can design, build, document, and deploy a database-backed REST API using
Django REST Framework, including token authentication, validated CRUD operations, and per-user permissions.

## The five-day journey

| Day | Date | Focus | Project increment | Daily proof |
|---|---|---|---|---|
| [1](../days/day-01/README.md) | Sun, Oct 25 | Foundations and setup | Repository, Django/DRF project, Task model, migrations, admin data | Server runs; Task records persist |
| [2](../days/day-02/README.md) | Tue, Oct 27 (with Day 3) | Core API: CRUD with function views | Five function views, five `path()` routes, complete CRUD endpoints | CRUD checklist passes; blank title → 400 |
| [3](../days/day-03/README.md) | Tue, Oct 27 (with Day 2) | Serialization and validation | `TaskSerializer` in every view, validation rules | invalid input → 400 with field errors |
| [4](../days/day-04/README.md) | Wed, Oct 28 (with Day 5) | Security and configuration | Token auth, ownership, data isolation; settings from the environment, deployment packages | Two-user security check passes |
| [5](../days/day-05/README.md) | Wed, Oct 28 (with Day 4) | Publish and demonstrate | Production deployment, smoke test, final README, demonstration | Live URL and final evidence pass |

## Daily session timing (about 3 hours)

| Block | Duration | Days 1-4 | Day 5 |
|---|---|---|---|
| 1. Explanation + live demo | ~60 min | instructor | instructor (includes a live deployment) |
| 2. Practice | ~60 min | **exercise** (Library API, core tasks first) | **guided deployment** of each participant's project |
| 3. Project | ~60 min | **project milestone** (Task API) | verify, README, submit |

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

### Day 1: Foundations, setup, and project start (Sunday, Oct 25)

- **Instructor explains (~60 min):** client and server; an annotated HTTP request and response (method, URL, headers,
  body, status code); what a web framework is and what Django/DRF do for you; HTTP verbs on the Task resource;
  project vs app; databases in depth (tables, rows, columns, primary and foreign keys, SQL vs the ORM); a short
  model → migration → admin demo; reproducibility (dependencies recorded, environments and secrets out of Git).
- **Exercise (~60 min):** Library catalog: `Book` model, migrations, sample data, admin (+ ORM practice as stretch).
- **Project (~60 min):** copy the starter, Task fields and status choices, owner → User, migrations, admin, two users,
  first GitHub push. If the push runs over, it finishes in the first 10 minutes of Day 2.
- **Completion criteria:** a fresh terminal activates the environment and starts the server; `migrate` reports no
  pending migrations; Task fields and status choices match the scope; admin creates, updates, and persists Task
  records with owners; the repository is pushed with no secrets or environment folder.

### Day 2: Core API, CRUD with function views (Tuesday, Oct 27, first half of the session)

- **Instructor explains (~60 min):** a function view (`@api_view`, `request.data`, `Response`, status codes); turning
  a model object into a dict by hand; `path()` routing with `<int:pk>` and URL names; the CRUD contract with one URL
  per operation; PUT vs PATCH; 200 / 201 / 204 / 400 / 404 / 405; a bad input that slips through (Day 3's motivation).
- **Exercise (~60 min):** Book CRUD API: `book_to_dict`, five function views, five `path()` routes (+ ordering and a
  CRUD checklist as stretch).
- **Project (~60 min):** `task_to_dict`, `list_tasks` / `create_task` / `get_task` / `update_task` / `delete_task`,
  five URLs, session login as a development bridge, owner set from `request.user`, blank title → 400.
- **Completion criteria:** every URL reaches its view (wrong method → 405); create → 201 and the row exists; retrieve →
  200, unknown id → 404; PUT/PATCH change only the intended fields; DELETE → 204; owner is server-assigned; blank
  title → 400.

### Day 3: Serialization and validation (Tuesday, Oct 27, second half of the session)

- **Instructor explains (~60 min):** the serializer as translator and gatekeeper; `ModelSerializer`, `fields`,
  `read_only_fields`, related fields with `source=`; serializers inside function views (`many=True`, `is_valid()`,
  `errors`, `save(owner=...)`, `partial`); validation: built-in rules, clearer messages with `extra_kwargs`,
  `validate_<field>`, `self.instance` (create vs update), object-level `validate()`.
- **Exercise (~60 min):** the Day 2 Book API with `BookSerializer` in every view and two validation rules (+ an
  object-level rule as stretch).
- **Project (~60 min):** `TaskSerializer` (owner and generated fields read-only), the five views rewritten with it,
  title error messages, due date not in the past on create (+ owner shown as username as stretch).
- **Completion criteria:** no view builds a dict by hand; read-only fields are protected; blank or missing title,
  invalid status, and a past creation due date → 400 with field errors; PUT without a title → 400, PATCH → 200.

### Day 4: Security and configuration (Wednesday, Oct 28, first half of the session)

- **Instructor explains (~60 min):** authentication vs authorization; tokens in the Authorization header; Postman with
  a token; two users show why authentication alone is insufficient (attack-and-fix demo); filtering every query by
  `request.user` and one owner-scoped lookup helper; 401 vs 403 vs 404; configuration from environment variables,
  `.env.example`, deployment packages.
- **Exercise (~60 min):** personal reading list: token login, ownership in every function view (+ user-aware
  validation as stretch).
- **Project (~60 min):** token support, token endpoint, owner-filtered list and `get_own_task`, the 8-step two-user
  scenario; settings from the environment, `.env.example`, deployment packages in `requirements.txt`.
- **Optional homework (~15 min):** open the Neon and Render accounts and read the deployment guide.
- **Completion criteria:** valid credentials return a token; no token → 401; a client-supplied owner is ignored; each
  list contains only the caller's records; cross-user access is blocked (404) without leaking data; production
  settings read from the environment; `pip check` is clean.

### Day 5: Deploy, verify, and submit (Wednesday, Oct 28, second half of the session)

- **Instructor explains (~60 min):** deployment as the same app under production configuration; a live deployment of
  the reference project; log reading by failure category; smoke tests and persistence; the evidence to submit.
- **Guided deployment (~60 min, replaces the exercise):** the `DATABASE_URL` setting (WhiteNoise, static files and CSRF
  origins come pre-written), Neon database, Render web service, environment variables, production users, everyone
  step by step with the instructor.
- **Project:** smoke test against the live URL and persistence check in the session; complete README and submission
  after the session, by the announced deadline. No live demo this cohort: the submitted evidence replaces it.
- **Completion criteria:** public HTTPS URL reachable with current migrations; token auth and CRUD work in production;
  isolation and validation pass live; a record survives restart/redeploy; the smoke test passes; the README lets a new reviewer
  set the project up from a fresh clone; the submission is complete.
