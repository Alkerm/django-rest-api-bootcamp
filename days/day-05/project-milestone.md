# Day 5 Project Milestone: Deploy, Verify, Demonstrate

**Project increment:** public HTTPS API with a persistent PostgreSQL database, a production smoke-test record, the
final README, and the live demonstration.
**Exit check:** the public HTTPS URL works, data persists, all required evidence is submitted, and the live demo passes.

> **Today the project comes first.** The Day 5 exercise is optional (the instructor demonstrates it). Start here
> right after the explanation block. Deployment takes longer than you think.

## Where to start

- **Finished Day 4?** Continue in your own repository. Copy `smoke_test.py` from
  [`project/checkpoints/day-05`](../../project/checkpoints/day-05), then apply the settings TODOs P1-P4 to your
  `config/settings.py` (each TODO comment in the checkpoint shows where the code goes).
- **Behind?** Copy the whole checkpoint over your project folder (keep `.git` and `.venv`).

## 1. Prepare the code (local)

| TODO | File | What | Hint |
|---|---|---|---|
| P1 | `config/settings.py` | use `DATABASE_URL` when it is set | [hints#p1](hints.md#p1) |
| P2 | `config/settings.py` | WhiteNoise middleware | [hints#p2](hints.md#p2) |
| P3 | `config/settings.py` | `STATIC_ROOT` + `STORAGES` | [hints#p3](hints.md#p3) |
| P4 | `config/settings.py` | `CSRF_TRUSTED_ORIGINS` from the environment | [hints#p4](hints.md#p4) |
| P5 | `.env.example` | add `DATABASE_URL` and `CSRF_TRUSTED_ORIGINS` placeholders | [hints#p5](hints.md#p5) |

Check locally, then push:

```bash
python manage.py test                       # all green
python manage.py collectstatic --noinput    # succeeds
git add . && git commit -m "Day 5: production settings" && git push
```

## 2. Deploy

Follow [`setup/deployment.md`](../../setup/deployment.md) step by step: Neon database → Render web service →
environment variables → build → production users.

Write down your public URL: `https://______________________.onrender.com`

## 3. Verify (smoke test)

Create two users in **production** (see the deployment guide), then:

```bash
python smoke_test.py --base-url https://<your-app>.onrender.com --user alice --other-user bob
```

Expected: `10/10 checks passed`.

**Persistence check:** create one task with Postman → Render **Manual Deploy → Restart service** (or redeploy) → list
the tasks again: it is still there.

## 4. Finish the README (P6)

Fill in the live URL and the Deployment section ([hints#p6](hints.md#p6)). Commit and push. Render redeploys
automatically.

## 5. Submit

| Evidence | Where |
|---|---|
| GitHub repository URL (accessible to reviewers) | submission form |
| Public HTTPS deployment URL | submission form + README |
| Passing test output (≥ 8 tests) | copy the `python manage.py test` output |
| Smoke-test output (10/10) | copy the terminal output (no tokens or passwords in it) |
| Completed Definition of Done checklist | [`project/project-brief.md`](../../project/project-brief.md#definition-of-done) |

## 6. Live demonstration (~5 minutes, at one of the 2-3 review stations)

Join the queue of any free station as soon as your smoke test passes; the stations run in parallel, so do not wait
until the end of the session.

Wake the service up a minute before. Then show, **on the live URL**:

1. Obtain a token and authenticate.
2. Create and list your tasks.
3. Update one task, then show a validation failure (`400`).
4. Prove data isolation: the second user gets `404` for your task.
5. Delete a task, then show that the remaining data persists (it survived a restart).

For each step: **state the claim → perform the request → point at the proof** (status code + body).

## Exit check

- [ ] The public HTTPS URL is reachable and production migrations are applied.
- [ ] Token authentication and all CRUD operations work in production.
- [ ] Two-user isolation and validation checks pass against the live URL.
- [ ] A created record survives a restart or redeploy.
- [ ] Automated tests pass, and the README contains final repository and deployment instructions.
- [ ] The submission includes repository URL, deployment URL, test evidence, and the completed checklist.
- [ ] The live demo completes without instructor code changes.

Optional improvements start **only** after every box above is checked (see the optional extensions in the
[project brief](../../project/project-brief.md#optional-extensions)).
