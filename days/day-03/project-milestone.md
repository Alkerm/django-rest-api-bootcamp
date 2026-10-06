# Day 3 Project Milestone: Authentication, Ownership, Permissions

**Project increment:** token login endpoint, protected routes, automatic owner, per-user isolation, cross-user
protection. (Validation was added on Day 2.)
**Exit check:** user A cannot view or modify user B's tasks, and requests without a token get `401`.

## Where to start

**Everyone does the same thing each morning:** copy today's checkpoint over your project. It contains everything up
to yesterday already solved, plus today's TODOs, so you never have to merge files by hand. Your Git history, your
`.venv` and your database (users and tasks) are kept.

Open a terminal in the folder that contains **both** `django-rest-api-bootcamp` and `task-management-api`:

```powershell
# Windows PowerShell
git -C django-rest-api-bootcamp pull       # only when the instructor announces an update
cd task-management-api
git add -A; git commit -m "End of Day 2"                       # save your own work first
Copy-Item -Path ..\django-rest-api-bootcamp\project\checkpoints\day-03\* -Destination . -Recurse -Force
.venv\Scripts\Activate.ps1
python manage.py migrate
```

```bash
# macOS
git -C django-rest-api-bootcamp pull       # only when the instructor announces an update
cd task-management-api
git add -A && git commit -m "End of Day 2"
cp -R ../django-rest-api-bootcamp/project/checkpoints/day-03/. .
source .venv/bin/activate
python manage.py migrate
```

> Curious how your Day 2 code compares with the reference? Run `git diff` before your next commit: the differences
> are a free code review. `nothing to commit` after `git commit` is fine.

## TODOs

| TODO | File | What | Hint |
|---|---|---|---|
| P1 | `config/settings.py` | add `rest_framework.authtoken`, then `migrate` | [hints#p1](hints.md#p1) |
| P2 | `config/settings.py` | `DEFAULT_AUTHENTICATION_CLASSES`: Token first, then Session | [hints#p2](hints.md#p2) |
| P3 | `config/urls.py` | import `obtain_auth_token`, add `api/auth/token/` (`name="api-token"`) | [hints#p3](hints.md#p3) |
| P4 | `tasks/views.py` | `get_queryset()` → only the caller's tasks | [hints#p4](hints.md#p4) |
| P5 | `tasks/permissions.py` | `IsOwner.has_object_permission` | [hints#p5](hints.md#p5) |
| P6 *(Day 2 review)* | `tasks/serializers.py` | show `owner` as the username | [hints#p6](hints.md#p6) |

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

Save evidence (screenshots or copied responses, **without tokens**) in your notes. You will automate all of this
tomorrow.

## Commit

```bash
git add .
git commit -m "Day 3: token auth, ownership, permissions"
git push
```

## Exit check

- [ ] Valid credentials return a token; protected routes reject requests without one (`401`).
- [ ] Authenticated creation ignores any client-supplied owner.
- [ ] Each user's list contains only their own records.
- [ ] Cross-user retrieve/update/delete is blocked (`404`) without leaking data.
- [ ] The two-user check is recorded and the commit is pushed.
