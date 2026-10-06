# Day 3: Authentication, Ownership, and Permissions

**Tuesday, October 13, 2026** · Focus: **Security** · [← Day 2](../day-02/README.md) · [Day 4 →](../day-04/README.md)

## Learning outcome

By the end of the session, you can secure the API with tokens, isolate each user's data, and enforce ownership at query and object level.

## Session flow (about 3 hours)

| Block | Time | What happens | Material |
|---|---|---|---|
| 1. Explanation + live demo | ~60 min | the instructor explains and builds in front of you | [`slides.md`](slides.md) · [`example/`](example/) |
| 2. Exercise | ~60 min | Personal reading list: token auth, then `get_queryset` + `perform_create`. **Core** tasks first, **stretch** only if time is left | [`exercise/README.md`](exercise/README.md) |
| 3. Project milestone | ~60 min | apply the same concept to **your** Task Management API | [`project-milestone.md`](project-milestone.md) |

Take a short break between blocks. The day ends with the **exit check** at the bottom of the milestone page.

**Priority rule:** the **project milestone** is what you are assessed on. If time is short, finish the exercise's
*core* tasks, move to the project, and come back to *stretch* tasks later.

## What the instructor explains (~60 min)

| Time | Topic |
|---|---|
| 10 min | Authentication (who is calling?) vs authorization (what may they do?); 401 vs 403 vs 404 in this program |
| 10 min | DRF tokens: the login endpoint, the `Authorization: Token <key>` header, why the token is a password |
| 10 min | Postman: an environment with `base_url` and `token`, sending the header |
| 20 min | Attack-and-fix demo with two users: bob reads alice's tasks → `get_queryset()` → bob gets 404; owner set in `perform_create` |
| 10 min | Defense in depth: read-only owner, `IsOwner` object permission |

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
