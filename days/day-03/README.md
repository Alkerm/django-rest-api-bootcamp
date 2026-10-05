# Day 3: Authentication, Ownership, and Validation

**Tuesday, October 13, 2026** · Focus: **Security** · [← Day 2](../day-02/README.md) · [Day 4 →](../day-04/README.md)

## Learning outcome

By the end of the session, you can secure the API with tokens, isolate each user's data, enforce ownership at query and object level, and return clear validation errors for realistic invalid input.

## Session flow (about 3-3.5 hours)

| Block | Time | What happens | Material |
|---|---|---|---|
| 1. Explanation + live demo | 45-60 min | the instructor explains and builds in front of you | [`slides.md`](slides.md) · [`example/`](example/) |
| Break / Q&A | 10 min | none | none |
| 2. Exercise | ~35 min core | practise today's concept on a small Library API: **core** tasks first, **stretch** only if time is left | [`exercise/README.md`](exercise/README.md) |
| 3. Project milestone | ~85 min | apply the same concept to **your** Task Management API | [`project-milestone.md`](project-milestone.md) |
| Exit check | 5-10 min | show the working result to a mentor | bottom of the milestone page |

About 30% of the session is explanation; at least 70% is hands-on work.

**Priority rule:** the **project milestone** is what you are assessed on. If time is short, finish the exercise's
*core* tasks, move to the project, and come back to *stretch* tasks later.

## What the instructor explains

- Authentication (who is calling?) vs authorization (what may they do?)
- DRF tokens: sent in the `Authorization` header on every request, protected like a password
- Two users show the problem: authentication alone is not enough if the queryset returns everyone's rows
- Defense in depth: filter by `request.user`, set the owner on the server, keep it read-only, check object permissions
- Validation as part of the API contract; 401 vs 403 vs 404 in this program

## Your materials for today

| Folder / file | Purpose |
|---|---|
| [`slides.md`](slides.md) | slides for this session (`slides.pdf` is added when ready) |
| [`example/`](example/) | a short worked example of today's concepts in a different domain: read it when you forget the syntax |
| [`exercise/`](exercise/) | **Personal reading list: token auth, `get_queryset` + `perform_create`, validation rules** (its own Django project and its own SQLite database) |
| [`hints.md`](hints.md) | step-by-step hints for every exercise task **and** every project TODO |
| [`solution/`](solution/) | the exercise solution, published by the instructor after the session |
| [`project-milestone.md`](project-milestone.md) | today's increment of the Task Management API, with its exit check |

## Stuck?

1. Re-read the TODO comment: it lists the field names, rules and expected results.
2. Open [`hints.md`](hints.md) one level at a time.
3. Compare with [`example/`](example/).
4. Check [`setup/troubleshooting.md`](../../setup/troubleshooting.md).
5. Ask a mentor, and bring the **exact error text**.
