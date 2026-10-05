# Day 5: Deploy, Verify, Improve, and Demonstrate

**Thursday, October 15, 2026** · Focus: **Publish** · [← Day 4](../day-04/README.md) · [Project brief →](../../project/project-brief.md)

## Learning outcome

By the end of the session, you can release the API to a public HTTPS environment, verify production behaviour and persistence, correct deployment issues, and demonstrate the completed system with evidence.

## Session flow (about 3-3.5 hours)

| Block | Time | What happens | Material |
|---|---|---|---|
| 1. Explanation + live demo | 45-60 min | the instructor explains and builds in front of you | [`slides.md`](slides.md) · [`example/`](example/) |
| Break / Q&A | 10 min | none | none |
| 2. Exercise | ~45 min | practise today's concept on a small Library API | [`exercise/README.md`](exercise/README.md) |
| 3. Project milestone | ~80 min | apply the same concept to **your** Task Management API | [`project-milestone.md`](project-milestone.md) |
| Exit check | 5-10 min | show the working result to a mentor | bottom of the milestone page |

About 30% of the session is explanation; at least 70% is hands-on work.

## What the instructor explains

- Deployment = the same application under production configuration: code, dependencies, variables, database, migrations, start command
- The release sequence: connect repo → provision service/database → set variables → build → migrate → start → verify
- Reading logs as evidence: configuration, dependencies, startup, host settings, or database connectivity?
- Smoke tests: authentication, one full CRUD path, validation, data isolation, persistence
- Technical demonstration: state the claim → act on the live system → point at visible proof

## Your materials for today

| Folder / file | Purpose |
|---|---|
| [`slides.md`](slides.md) | slides for this session (`slides.pdf` is added when ready) |
| [`example/`](example/) | a short worked example of today's concepts in a different domain: read it when you forget the syntax |
| [`exercise/`](exercise/) | **Production readiness: `DATABASE_URL`, WhiteNoise + `collectstatic`, a smoke test** (its own Django project and its own SQLite database) |
| [`hints.md`](hints.md) | step-by-step hints for every exercise task **and** every project TODO |
| [`solution/`](solution/) | the exercise solution, published by the instructor after the session |
| [`project-milestone.md`](project-milestone.md) | today's increment of the Task Management API, with its exit check |

## Stuck?

1. Re-read the TODO comment: it lists the field names, rules and expected results.
2. Open [`hints.md`](hints.md) one level at a time.
3. Compare with [`example/`](example/).
4. Check [`setup/troubleshooting.md`](../../setup/troubleshooting.md).
5. Ask a mentor, and bring the **exact error text**.
