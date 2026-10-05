# Day 4: Testing, Quality, Documentation, and Delivery

**Wednesday, October 14, 2026** · Focus: **Quality** · [← Day 3](../day-03/README.md) · [Day 5 →](../day-05/README.md)

## Learning outcome

By the end of the session, you can verify API behaviour with automated tests, document a reproducible setup, protect configuration secrets, and complete a deployment rehearsal with production-ready settings.

## Session flow (about 3-3.5 hours)

| Block | Time | What happens | Material |
|---|---|---|---|
| 1. Explanation + live demo | 45-60 min | the instructor explains and builds in front of you | [`slides.md`](slides.md) · [`example/`](example/) |
| Break / Q&A | 10 min | none | none |
| 2. Exercise | ~45 min core | practise today's concept on a small Library API: **core** tasks first, **stretch** only if time is left | [`exercise/README.md`](exercise/README.md) |
| 3. Project milestone | ~80 min | apply the same concept to **your** Task Management API | [`project-milestone.md`](project-milestone.md) |
| Exit check | 5-10 min | show the working result to a mentor | bottom of the milestone page |

About 30% of the session is explanation; at least 70% is hands-on work.

**Priority rule:** the **project milestone** is what you are assessed on. If time is short, finish the exercise's
*core* tasks, move to the project, and come back to *stretch* tasks later.

## What the instructor explains

- A test as an executable promise: arrange known data, perform one action, assert the response and database effect
- Positive and failure tests: allowed work succeeds, forbidden or invalid work fails correctly
- Test isolation: every test creates its own users and tasks
- Production configuration: `DEBUG` off, secrets and database from environment variables, recorded dependencies
- The README as part of the product: clone, configure, test, and use without verbal rescue

## Your materials for today

| Folder / file | Purpose |
|---|---|
| [`slides.md`](slides.md) | slides for this session (`slides.pdf` is added when ready) |
| [`example/`](example/) | a short worked example of today's concepts in a different domain: read it when you forget the syntax |
| [`exercise/`](exercise/) | **Test the reading-list API (8 tests) + settings from environment variables** (its own Django project and its own SQLite database) |
| [`hints.md`](hints.md) | step-by-step hints for every exercise task **and** every project TODO |
| [`solution/`](solution/) | the exercise solution, published by the instructor after the session |
| [`project-milestone.md`](project-milestone.md) | today's increment of the Task Management API, with its exit check |

## Stuck?

1. Re-read the TODO comment: it lists the field names, rules and expected results.
2. Open [`hints.md`](hints.md) one level at a time.
3. Compare with [`example/`](example/).
4. Check [`setup/troubleshooting.md`](../../setup/troubleshooting.md).
5. Ask a mentor, and bring the **exact error text**.
