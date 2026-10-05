# Day 3 Project Milestone: Authentication, Ownership, Validation

**Project increment:** token login endpoint, protected routes, automatic owner, per-user isolation, cross-user
protection, validation.
**Exit check:** user A cannot view or modify user B's tasks, and invalid data is rejected with field-level errors.

## Where to start

- **Finished Day 2?** Continue in your own repository. Create `tasks/permissions.py` by copying it from
  [`project/checkpoints/day-03`](../../project/checkpoints/day-03), then apply the TODOs below to your files.
  Each TODO comment in the checkpoint shows exactly where the code goes.
- **Behind?** Copy the checkpoint's files over your project folder (keep `.git` and `.venv`), then run
  `python manage.py migrate`.

## TODOs

| TODO | File | What | Hint |
|---|---|---|---|
| P1 | `config/settings.py` | add `rest_framework.authtoken`, then `migrate` | [hints#p1](hints.md#p1) |
| P2 | `config/settings.py` | `DEFAULT_AUTHENTICATION_CLASSES`: Token first, then Session | [hints#p2](hints.md#p2) |
| P3 | `config/urls.py` | import `obtain_auth_token`, add `api/auth/token/` (`name="api-token"`) | [hints#p3](hints.md#p3) |
| P4 | `tasks/views.py` | `get_queryset()` → only the caller's tasks | [hints#p4](hints.md#p4) |
| P5 | `tasks/permissions.py` | `IsOwner.has_object_permission` | [hints#p5](hints.md#p5) |
| P6 *(Day 2 review)* | `tasks/serializers.py` | show `owner` as the username | [hints#p6](hints.md#p6) |
| P7 | `tasks/serializers.py` | clear title errors: `Title is required.` / `Title cannot be blank.` | [hints#p7](hints.md#p7) |
| P8 | `tasks/serializers.py` | `validate_due_date`: not before today, **on create only** | [hints#p8](hints.md#p8) |

## The two-user security check (record the results)

Use Postman (see [`setup/postman.md`](../../setup/postman.md)) with the two users you created on Day 1.
Make sure **each** user owns at least one task (use the admin if needed).

| # | Request | Expected |
|---|---|---|
| 1 | `POST /api/auth/token/` alice's credentials | `200` + token |
| 2 | `POST /api/auth/token/` wrong password | `400` |
| 3 | `GET /api/tasks/` **without** token | `401` |
| 4 | alice: `GET /api/tasks/` | `200`, only alice's tasks, `"owner": "alice"` |
| 5 | alice: `POST /api/tasks/` `{"title": "Mine", "owner": <bob's id>}` | `201`, owner `alice` |
| 6 | bob: `GET /api/tasks/{alice's task id}/` | `404` |
| 7 | bob: `PATCH /api/tasks/{alice's task id}/` `{"title": "x"}` | `404`, alice's task unchanged |
| 8 | bob: `DELETE /api/tasks/{alice's task id}/` | `404`, task still exists |
| 9 | alice: `POST /api/tasks/` `{"title": "   "}` | `400` `{"title": ["Title cannot be blank."]}` |
| 10 | alice: `POST /api/tasks/` `{"title": "X", "status": "FINISHED"}` | `400` `status` error |
| 11 | alice: `POST /api/tasks/` `{"title": "X", "due_date": "2020-01-01"}` | `400` `{"due_date": ["Due date cannot be earlier than today."]}` |

Save evidence (screenshots or copied responses, **without tokens**) in your notes. You will automate all of this
tomorrow.

## Commit

```bash
git add .
git commit -m "Day 3: token auth, ownership, validation"
git push
```

## Exit check

- [ ] Valid credentials return a token; protected routes reject requests without one (`401`).
- [ ] Authenticated creation ignores any client-supplied owner.
- [ ] Each user's list contains only their own records.
- [ ] Cross-user retrieve/update/delete is blocked (`404`) without leaking data.
- [ ] Blank title, invalid status, and a past due date on create return `400`.
- [ ] The two-user check is recorded and the commit is pushed.
