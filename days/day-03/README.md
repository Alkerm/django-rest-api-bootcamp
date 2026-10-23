# Day 3: Serialization and Validation

**Tuesday, October 27, 2026** · Focus: **Serialization** · [← Day 2](../day-02/README.md) · [Day 4 →](../day-04/README.md)

## Learning outcome

By the end of the session, you can replace hand-written conversion code with a `ModelSerializer`, use it in function
views to validate input and save data, tell PUT and PATCH apart with `partial`, and reject invalid input with clear
field-level errors.

## Session flow (about 3 hours)

| Block | Time | What happens | Material |
|---|---|---|---|
| 1. Explanation + live demo | ~60 min | the instructor explains and builds in front of you | [`slides.md`](slides.md) · [`example/`](example/) |
| 2. Exercise | ~60 min | Book API: `BookSerializer`, the five views rewritten with it, two validation rules. **Core** tasks first, **stretch** only if time is left | [`exercise/README.md`](exercise/README.md) |
| 3. Project milestone | ~60 min | apply the same concept to **your** Task Management API | [`project-milestone.md`](project-milestone.md) |

Take a short break between blocks. The day ends with the **exit check** at the bottom of the milestone page.

**Priority rule:** the **project milestone** is what you are assessed on. If time is short, finish the exercise's
*core* tasks, move to the project, and come back to *stretch* tasks later.

## What the instructor explains (~60 min)

| Time | Topic |
|---|---|
| 10 min | Yesterday's pain: show a bad `status` being saved and a bad date crashing with 500. What we need: one place for "object ⇄ JSON" and "is this input valid?" |
| 15 min | The serializer as translator (model ⇄ JSON) and gatekeeper: `ModelSerializer`, `fields`, `read_only_fields`, a related field with `source=`; try it in `python manage.py shell` |
| 15 min | Serializers in function views: `many=True`, `data=`, `is_valid()`, `serializer.errors`, `save(owner=...)`, `partial` for PATCH; one POST traced end to end |
| 15 min | Validation: built-in rules, clearer messages with `extra_kwargs`, your own rule with `validate_<field>`, `self.instance` (create vs update), object-level `validate()` |
| 5 min | Live demo in the browsable API: the same five URLs, now with 400s and field errors |

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
