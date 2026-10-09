# Day 2: Core API: CRUD and Validation

**Monday, October 26, 2026** · Focus: **Core API** · [← Day 1](../day-01/README.md) · [Day 3 →](../day-03/README.md)

## Learning outcome

By the end of the session, you can convert Task objects to validated JSON, implement routed create, list, retrieve, update, partial-update, and delete operations, and reject invalid input with clear field-level errors.

## Session flow (about 3 hours)

| Block | Time | What happens | Material |
|---|---|---|---|
| 1. Explanation + live demo | ~60 min | the instructor explains and builds in front of you | [`slides.md`](slides.md) · [`example/`](example/) |
| 2. Exercise | ~60 min | Book CRUD API: serializer, viewset, router, two validation rules. **Core** tasks first, **stretch** only if time is left | [`exercise/README.md`](exercise/README.md) |
| 3. Project milestone | ~60 min | apply the same concept to **your** Task Management API | [`project-milestone.md`](project-milestone.md) |

Take a short break between blocks. The day ends with the **exit check** at the bottom of the milestone page.

**Priority rule:** the **project milestone** is what you are assessed on. If time is short, finish the exercise's
*core* tasks, move to the project, and come back to *stretch* tasks later.

## What the instructor explains (~60 min)

| Time | Topic |
|---|---|
| 10 min | The serializer as translator (model ⇄ JSON) and gatekeeper (rejects invalid input before saving) |
| 15 min | ViewSets and routers: one class, six operations, predictable list/detail URLs; the CRUD contract with its status codes |
| 10 min | One POST traced end to end: JSON → validation → save → row → serialized response → 201; PUT vs PATCH |
| 15 min | Validation: built-in rules, clearer messages with `extra_kwargs`, your own rule with `validate_<field>`, and `self.instance` (create vs update) |
| 10 min | Live demo in the browsable API: every endpoint, a 400 with field errors, a 404 |

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
