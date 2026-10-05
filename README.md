# Building REST APIs with Django

**Tuwaiq Club at KFUPM** · Modern Software & Cloud track · **October 11-15, 2026** · five hands-on days

In five days you design, build, test, document, and deploy a **database-backed REST API** with
**Django REST Framework**, including token authentication, validated CRUD operations, and per-user permissions.
You leave with a live, portfolio-ready backend: your own **Personal Task Management API**.

---

## How every day works

```text
 1. Learn                      2. Practise                        3. Apply                                4. Prove
 instructor explains + demos → days/day-0X/exercise/            → days/day-0X/project-milestone.md      → exit check
 (slides, example/)             a small Library API with its     today's increment of YOUR Task API,
                                own database, tasks + hints       built a bit more every day
```

Each topic is learned once, practised on the **exercise**, then applied to the **project**. By Day 5 the project is
complete and deployed.

| Day | Date | Focus | Exercise (Library API) | Project increment (your Task API) |
|---|---|---|---|---|
| [1](days/day-01/README.md) | Sun, Oct 11 | Foundation | Book model, migrations, sample data, admin, ORM | Django project, `Task` model, admin, GitHub repo |
| [2](days/day-02/README.md) | Mon, Oct 12 | Core API | Book CRUD API with serializer, viewset, router | Complete CRUD at `/api/tasks/` |
| [3](days/day-03/README.md) | Tue, Oct 13 | Security | Personal reading list: tokens, ownership, validation | Token login, per-user isolation, validation |
| [4](days/day-04/README.md) | Wed, Oct 14 | Quality | Write 8 API tests, settings from environment | ≥ 8 tests, README, env config, deploy rehearsal |
| [5](days/day-05/README.md) | Thu, Oct 15 | Publish | *optional*: `DATABASE_URL`, static files, smoke test | Live HTTPS deployment, smoke test, demo |

Daily session: **3-3.5 hours**, made up of 45-60 min explanation and demo, a 10 min break, and 2-2.25 h hands-on.

## Start here

1. Check the [prerequisites](setup/prerequisites.md).
2. Follow the [installation guide](setup/installation.md) and finish the **readiness check before Day 1**.
3. Read the [project brief](project/project-brief.md): it describes what you will have built by Day 5.
4. On each day, open `days/day-0X/README.md`.

## Repository map

```text
README.md                    ← you are here
requirements.txt             shared environment for all exercises
program/
  program-brief.md           purpose, audience, milestones, evidence of completion
  learning-outcomes.md       what you will be able to do
  five-day-agenda.md         the detailed daily plan and timing
setup/
  prerequisites.md           knowledge, laptop, accounts
  installation.md            install + readiness check (Windows and macOS)
  troubleshooting.md         common errors + recovery plan
  postman.md                 using the Postman collection
  deployment.md              Render + Neon runbook (Day 5)
days/day-01 … day-05/
  README.md                  outcome, session flow, topics
  slides.md                  slides (slides.pdf is added when ready)
  example/                   worked example of the day's concepts (different domain)
  exercise/                  the day's exercise: its own Django project + SQLite DB + README with tasks
  hints.md                   step-by-step hints for the exercise AND the project TODOs
  solution/                  exercise solution (released by the instructor after the session)
  project-milestone.md       today's project increment + exit check
project/
  project-brief.md           requirements, API contract, Definition of Done, rubric
  starter/                   Day 1 starting point of your project
  checkpoints/day-02 … 05    start of each day: previous days solved + new TODOs (also your recovery point)
  reference-solution/        complete project (instructor repository)
assets/
  postman/                   Postman collection for the Task API
  source-documents/          the original program PDFs
```

## Conventions you will see in the code

```python
# TODO [Day 3 · P4]: what to write, with the exact names and rules
# HINT: days/day-03/hints.md#p4  |  Example: days/day-03/example/views.py
# YOUR CODE HERE
pass                    # placeholder that keeps the file runnable until you replace it
```

- `Task 1`, `Task 2`, … are exercise tasks. `P1`, `P2`, … are project TODOs.
- **Core vs stretch:** exercise tasks marked **STRETCH (optional)** are extra practice for fast finishers. Do the
  core tasks, then the **project milestone** (that is what is assessed), and come back to stretch tasks if time is left.
  On Day 4 the project's tests are labelled **REQUIRED** (8 in total) or **STRETCH**.
- Lines marked **GIVEN** are complete. Read them, because they are often the pattern for your TODO.
- Each exercise starts with **Before you start** (commands, database state, sample data) and lists the expected
  input, database change, and output next to every task.

## Stack

Python 3.13 · Django 5.2 LTS · Django REST Framework 3.16 · SQLite + DB Browser · Postman · Git + GitHub ·
Render (free) + Neon PostgreSQL (free). Every required tool and service is **free**.

## Rules that keep everyone on track

- **Secrets never go into Git.** That means passwords, tokens, `SECRET_KEY`, and database URLs. `.env.example` holds placeholders only.
- **Required work first.** Optional extensions start only after the day's exit check passes.
- **Fell behind?** Start the next day from `project/checkpoints/day-0X`. You lose nothing, and Day 5 stays reachable.
- **Asking for help:** bring the exact command and the complete error text.
