# Day 4: Security and Configuration

**Wednesday, October 28, 2026** · Focus: **Security** · [← Day 3](../day-03/README.md) · [Day 5 →](../day-05/README.md)

## Learning outcome

By the end of the session, you can secure the API with tokens, isolate each user's data in every function view, and
move secrets and environment-specific settings out of the code so the project is ready to deploy.

## Session flow (about 3 hours)

| Block | Time | What happens | Material |
|---|---|---|---|
| 1. Explanation + live demo | ~60 min | the instructor explains and builds in front of you | [`slides.md`](slides.md) · [`example/`](example/) |
| 2. Exercise | ~60 min | Personal reading list: token auth, then ownership in every view. **Core** tasks first, **stretch** only if time is left | [`exercise/README.md`](exercise/README.md) |
| 3. Project milestone | ~60 min | apply the same concept to **your** Task Management API, then prepare its configuration for Day 5 | [`project-milestone.md`](project-milestone.md) |

Take a short break between blocks. The day ends with the **exit check** at the bottom of the milestone page.

**Priority rule:** the **project milestone** is what you are assessed on. If time is short, finish the exercise's
*core* tasks, move to the project, and come back to *stretch* tasks later.

## What the instructor explains (~60 min)

| Time | Topic |
|---|---|
| 10 min | Authentication (who is calling?) vs authorization (what may they do?); 401 vs 403 vs 404 in this program |
| 10 min | DRF tokens: the login endpoint, the `Authorization: Token <key>` header, why the token is a password; Postman with `base_url` and `token` |
| 20 min | Attack-and-fix demo with two users: bob reads alice's tasks → filter every query by `request.user` → bob gets 404; one `get_own_task()` helper for get/update/delete; owner set on `save()` |
| 15 min | Configuration: why `DEBUG`, `SECRET_KEY` and hosts come from environment variables; `.env.example`; deployment packages in `requirements.txt` |
| 5 min | Preview of Day 5 (deployment) and the optional homework |

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
