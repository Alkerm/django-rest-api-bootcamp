# Day 5 Project Milestone: Deploy, Verify, Demonstrate

**Project increment:** public HTTPS API with a persistent PostgreSQL database, a production smoke-test record, the
final README, and the live demonstration.
**Exit check:** the public HTTPS URL works, data persists, all required evidence is submitted, and the live demo passes.

> **Today has no exercise hour.** After the explanation, the second hour is a **guided deployment**: everyone does
> steps 1-2 below together with the instructor. The third hour is for verifying, finishing the README, submitting and
> demonstrating (steps 3-6). The Library exercise for Day 5 is optional homework.

| Hour | What you do |
|---|---|
| 1 | Explanation + the instructor deploys the reference project live |
| 2 | **Guided deployment:** steps 1-2 (`DATABASE_URL` setting, Neon, Render, production users) |
| 3 | Steps 3-6: smoke test, persistence, README, submission, live demo at a review station |

## Where to start

Open a terminal in the folder that contains **both** `django-rest-api-bootcamp` and `task-management-api`.

**Finished Day 4?** Copy **only these three files**, so your own README and tests (written yesterday and graded) stay
yours:

```powershell
# Windows PowerShell
git -C django-rest-api-bootcamp pull       # only when the instructor announces an update
cd task-management-api
git add -A; git commit -m "End of Day 4"
$cp = "..\django-rest-api-bootcamp\project\checkpoints\day-05"
Copy-Item "$cp\config\settings.py" config\ -Force
Copy-Item "$cp\.env.example", "$cp\smoke_test.py" . -Force
.venv\Scripts\Activate.ps1
```

```bash
# macOS
git -C django-rest-api-bootcamp pull       # only when the instructor announces an update
cd task-management-api
git add -A && git commit -m "End of Day 4"
cp ../django-rest-api-bootcamp/project/checkpoints/day-05/config/settings.py config/
cp ../django-rest-api-bootcamp/project/checkpoints/day-05/{.env.example,smoke_test.py} .
source .venv/bin/activate
```

**Behind?** Copy the **whole** checkpoint instead (same command as on Days 2-4, with `day-05`), then
`python -m pip install -r requirements.txt` and `python manage.py migrate`. This also replaces `README.md` and
`tasks/tests.py` with the reference versions: review them, and make the README your own before you submit.

## 1. Prepare the code (local) · hour 2

| TODO | File | What | Hint |
|---|---|---|---|
| P1 | `config/settings.py` | use `DATABASE_URL` when it is set | [hints#p1](hints.md#p1) |
| P2 | `.env.example` | add `DATABASE_URL` and `CSRF_TRUSTED_ORIGINS` placeholders | [hints#p2](hints.md#p2) |

WhiteNoise, static files, `CSRF_TRUSTED_ORIGINS` and a production-safe `DEBUG` default are **already written** in the settings you copied (marked
`GIVEN`): read them, so you know what Render needs.

Check locally, then push:

```bash
python manage.py test                       # all green
python manage.py collectstatic --noinput    # succeeds
git add . && git commit -m "Day 5: production settings" && git push
```

## 2. Deploy · hour 2

Follow [`setup/deployment.md`](../../setup/deployment.md) step by step: Neon database → Render web service →
environment variables → build → production users.

Write down your public URL: `https://______________________.onrender.com`

## 3. Verify (smoke test) · hour 3

Create two users in **production** (see the deployment guide), then:

```bash
python smoke_test.py --base-url https://<your-app>.onrender.com --user alice --other-user bob
```

Expected: `10/10 checks passed`.

**Persistence check:** create one task with Postman → Render **Manual Deploy → Restart service** (or redeploy) → list
the tasks again: it is still there.

## 4. Finish the README (P3) · hour 3

Complete every `_TODO_` section of the README you received on Day 4, add the live URL at the top, and write the
Deployment section ([hints#p3](hints.md#p3)). Commit and push. Render redeploys automatically.

If a classmate is free, ask them to follow your README from a fresh clone. Every place they had to guess is a
sentence to add.

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
- [ ] Automated tests pass, and the README contains setup, tests, authentication, endpoint examples, the live URL and
  deployment instructions, so a new reviewer can set the project up from a fresh clone.
- [ ] The submission includes repository URL, deployment URL, test evidence, and the completed checklist.
- [ ] The live demo completes without instructor code changes.

Optional improvements start **only** after every box above is checked (see the optional extensions in the
[project brief](../../project/project-brief.md#optional-extensions)).
