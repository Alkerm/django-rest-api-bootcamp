# Day 1: Foundations, Setup, and Project Start

**Sunday, October 25, 2026** · Focus: **Foundation** · [← Program overview](../../README.md) · [Day 2 →](../day-02/README.md)

## Learning outcome

By the end of the session, you can explain the basic HTTP request-response flow, run a reproducible Django REST Framework environment, and persist Task records through a correctly migrated data model.

## Session flow (about 3 hours)

| Block | Time | What happens | Material |
|---|---|---|---|
| 1. Explanation + live demo | ~60 min | the instructor explains and builds in front of you | [`slides.md`](slides.md) · [`example/`](example/) |
| 2. Exercise | ~60 min | Library catalog: complete the `Book` model, migrate, load sample data, admin (ORM practice is stretch). **Core** tasks first, **stretch** only if time is left | [`exercise/README.md`](exercise/README.md) |
| 3. Project milestone | ~60 min | apply the same concept to **your** Task Management API | [`project-milestone.md`](project-milestone.md) |

Take a short break between blocks. The day ends with the **exit check** at the bottom of the milestone page.

**Priority rule:** the **project milestone** is what you are assessed on. If time is short, finish the exercise's
*core* tasks, move to the project, and come back to *stretch* tasks later.

> If the first GitHub push runs over, finish it in the first 10 minutes of Day 2.

## What the instructor explains (~60 min)

| Time | Topic |
|---|---|
| 10 min | The finished project first: request → Django → DRF → ORM → database → JSON + status code |
| 10 min | HTTP verbs on the Task resource: GET reads, POST creates, PUT/PATCH change, DELETE removes; the URL names the resource, the verb names the action |
| 10 min | Django structure: the **project** (`config/`) holds global configuration, the **app** (`tasks/`) owns behavior, DRF adds API tools on top |
| 25 min | Live demo: a model → `makemigrations` → `migrate` → admin → a few ORM queries in the shell |
| 5 min | Reproducibility: virtual environment, `requirements.txt`, `.gitignore`, secrets outside Git |

## Your materials for today

| Folder / file | Purpose |
|---|---|
| [`slides.md`](slides.md) | slides for this session (`slides.pdf` is added when ready) |
| [`example/`](example/) | a short worked example of today's concepts in a different domain: read it when you forget the syntax |
| [`exercise/`](exercise/) | today's exercise: its own Django project and its own SQLite database |
| [`hints.md`](hints.md) | step-by-step hints for every exercise task **and** every project TODO |
| [`solution/`](solution/) | the exercise solution, published by the instructor after the session |
| [`project-milestone.md`](project-milestone.md) | today's increment of the Task Management API, with its exit check |

## Stuck?

1. Re-read the TODO comment: it lists the field names, rules and expected results.
2. Open [`hints.md`](hints.md) one level at a time.
3. Compare with [`example/`](example/).
4. Check [`setup/troubleshooting.md`](../../setup/troubleshooting.md).
5. Ask a mentor, and bring the **exact error text**.
