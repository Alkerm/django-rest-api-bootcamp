# Day 5: Deploy, Verify, and Demonstrate

**Wednesday, October 28, 2026 (second half of the session)** · Focus: **Publish** · [← Day 4](../day-04/README.md) · [Project brief →](../../project/project-brief.md)

> **Schedule change (Monday's session was cancelled).** This day is taught **together with Day 4** in one session: **Wednesday, October 28, 8:00-10:00 PM**. The instructor goes through both days' slides quickly and may solve some exercise tasks live; then you work on the **project**. **All exercises are optional**: do them later for practice. The "Session flow" table below describes the original 3-hour day.
>
> **Deploy in the session, submit afterwards:** the README, the submission form and the smoke-test evidence are
> due by the deadline your instructors announce. The live demonstration is replaced by the submitted evidence.

## Learning outcome

By the end of the session, you can release the API to a public HTTPS environment, verify production behavior and persistence, correct deployment issues, and demonstrate the completed system with evidence.

## Session flow (about 3 hours)

| Block | Time | What happens | Material |
|---|---|---|---|
| 1. Explanation + live demo | ~60 min | the instructor explains and builds in front of you | [`slides.md`](slides.md) · [`example/`](example/) |
| 2. Guided deployment | ~60 min | Everyone deploys their own project together, step by step (milestone steps 1-2). The Library exercise is optional homework today | [`project-milestone.md`](project-milestone.md) |
| 3. Project milestone | ~60 min | verify in the session; finish the README and submit afterwards | [`project-milestone.md`](project-milestone.md) |

Take a short break between blocks. The day ends with the **exit check** at the bottom of the milestone page.

**Priority rule:** the **project milestone** is what you are assessed on. If time is short, finish the exercise's
*core* tasks, move to the project, and come back to *stretch* tasks later.

## What the instructor explains (~60 min)

| Time | Topic |
|---|---|
| 10 min | Deployment = the same application under production configuration: code, dependencies, variables, database, migrations, start command |
| 25 min | Live demo: deploy the reference project on Render + Neon, following `setup/deployment.md` |
| 10 min | Reading logs as evidence: configuration, dependencies, startup, host settings, or database connectivity? |
| 10 min | Smoke tests and persistence; the README as part of the product |
| 5 min | The evidence to submit: live URL, README, smoke-test output (no live demo this cohort) |

## Your materials for today

| Folder / file | Purpose |
|---|---|
| [`slides.md`](slides.md) | slides for this session (`slides.pdf` is added when ready) |
| [`example/`](example/) | a short worked example of today's concepts in a different domain: read it when you forget the syntax |
| [`exercise/`](exercise/) | today's exercise: its own Django project and its own SQLite database (optional today) |
| [`hints.md`](hints.md) | step-by-step hints for every exercise task **and** every project TODO |
| [`solution/`](solution/) | the exercise solution, published by the instructor after the session |
| [`project-milestone.md`](project-milestone.md) | today's increment of the Task Management API, with its exit check |

## Stuck?

1. Re-read the TODO comment: it lists the field names, rules and expected results.
2. Open [`hints.md`](hints.md) one level at a time.
3. Compare with [`example/`](example/).
4. Check [`setup/troubleshooting.md`](../../setup/troubleshooting.md).
5. Ask a mentor, and bring the **exact error text**.
