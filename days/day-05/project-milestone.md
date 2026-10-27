# Day 5 Project Milestone: Finish, Verify, Submit

**Project increment:** the final README, a passing smoke test against your local server, and the submission.
**Exit check:** the API works end to end locally, the README lets a classmate set it up from a fresh clone, and the
submission is sent.

> **Combined session (Wednesday, 8:00-10:00 PM):** Day 5 follows Day 4 in the same session. **Deployment is cancelled
> for this cohort**: everything runs on your laptop. Start the README and the smoke test in the session; the
> submission is due **after the session**, by the deadline your instructors announce.

## Where to start

**Nothing to copy today.** The Day 5 TODO (`TODO [Day 5 · P1]` in `README.md`) is already in your project: it came
with the final `day-04` checkpoint you copied at the start of the session. Just continue in `task-management-api`:

```bash
cd task-management-api
git add -A
git commit -m "Day 4: token auth, ownership, environment configuration"
```

Missed Day 4? Run **Step 0** of [the Day 4 milestone](../day-04/project-milestone.md) first, then come back here.

## 1. Verify (smoke test)

`smoke_test.py` (in your project) checks the whole API in one run: 401 without a token, login for two users,
create, list, update, a validation error, cross-user isolation, delete.

Make sure you have two users (e.g. `alice` and `bob`, created in the admin on Day 1). Then:

```bash
python manage.py runserver
```
Keep it running, and in a **second** terminal (same folder, `.venv` active):

```bash
python smoke_test.py --base-url http://127.0.0.1:8000 --user alice --other-user bob
```

It asks for both passwords. Expected: `10/10 checks passed.` A failing line names the behavior that is broken: fix it
in your code and run the script again. Hint: [hints#smoke](hints.md#smoke).

## 2. Finish the README (P1)

Complete every `_TODO_` section of `README.md`, including the **Check it (smoke test)** section
([hints#p1](hints.md#p1)). Commit and push.

If a classmate is free, ask them to follow your README from a fresh clone. Every place they had to guess is a
sentence to add.

## 3. Submit · after the session, before the announced deadline

Submit everything through the **[submission form](https://forms.gle/SjbXGzfP1zYCdjfN8)** once your smoke test passes and your README is
complete. Have these ready to paste:

| Evidence | Where |
|---|---|
| GitHub repository URL (accessible to reviewers) | [submission form](https://forms.gle/SjbXGzfP1zYCdjfN8) |
| Smoke-test output (10/10) against your local server | copy the terminal output into the form (no tokens or passwords in it) |
| Completed Definition of Done checklist | tick every item in the form ([`project/project-brief.md`](../../project/project-brief.md#definition-of-done)) |

Typed a wrong link? Use **Edit your response** on the confirmation page, or tell your instructors.

Reviewers clone your repository and follow your README, so make sure all of this works **from your README alone**:

1. Set up the project and create two users.
2. Obtain a token and authenticate.
3. Create, list, update and delete tasks; show a validation failure (`400`).
4. The second user gets `404` for the first user's task.

## Exit check

- [ ] `python smoke_test.py ...` prints `10/10 checks passed` against your local server.
- [ ] Token authentication, all CRUD operations, two-user isolation and validation work.
- [ ] The README contains setup, environment variables, migrations, authentication, endpoint examples and the
  smoke-test command, so a new reviewer can set the project up from a fresh clone.
- [ ] The repository has no secrets (`.env`, `db.sqlite3` and `.venv` are not in Git).
- [ ] The submission includes the repository URL, the smoke-test output, and the completed checklist.

Optional improvements start **only** after every box above is checked (see the optional extensions in the
[project brief](../../project/project-brief.md#optional-extensions)). Deploying the API to Render + Neon is one of
them: [`setup/deployment.md`](../../setup/deployment.md) still describes it.
