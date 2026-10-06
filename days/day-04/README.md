# Day 4: Testing and Configuration

**Wednesday, October 14, 2026** · Focus: **Quality** · [← Day 3](../day-03/README.md) · [Day 5 →](../day-05/README.md)

## Learning outcome

By the end of the session, you can verify API behaviour with automated tests, read a failing test to find a bug, and move configuration and secrets into environment variables.

## Session flow (about 3 hours)

| Block | Time | What happens | Material |
|---|---|---|---|
| 1. Explanation + live demo | ~60 min | the instructor explains and builds in front of you | [`slides.md`](slides.md) · [`example/`](example/) |
| 2. Exercise | ~60 min | Test the reading-list API: 4 required tests. **Core** tasks first, **stretch** only if time is left | [`exercise/README.md`](exercise/README.md) |
| 3. Project milestone | ~60 min | apply the same concept to **your** Task Management API | [`project-milestone.md`](project-milestone.md) |

Take a short break between blocks. The day ends with the **exit check** at the bottom of the milestone page.

**Priority rule:** the **project milestone** is what you are assessed on. If time is short, finish the exercise's
*core* tasks, move to the project, and come back to *stretch* tasks later.

## What the instructor explains (~60 min)

| Time | Topic |
|---|---|
| 10 min | A test as an executable promise: arrange known data, perform one action, assert the response and the database effect |
| 10 min | `APITestCase`, `setUp`, test isolation, tokens in tests; positive tests and failure tests |
| 20 min | Live demo: a 401 test and a cross-user test; break the app on purpose and read the failure; fix the app, not the test |
| 15 min | Configuration: why `DEBUG`, `SECRET_KEY` and hosts come from environment variables; `.env.example`; deployment packages |
| 5 min | Preview of Day 5 and the optional homework (accounts, deployment guide) |

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
