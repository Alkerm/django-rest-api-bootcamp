"""
Automated API tests for the Task Management API.

Run them with:   python manage.py test
Each test is an executable promise:  ARRANGE known data -> ACT (one request) -> ASSERT status + body + database.

The test runner builds a brand-new, empty test database for every run, so these tests never touch
your db.sqlite3 data, and each test starts from the same setUp() state (order does not matter).

Requirement: at least 8 meaningful tests pass.
  * 1 test is complete (the example).
  * 7 tests are marked REQUIRED  -> write these. Together with the example they make the 8 required tests.
  * 7 tests are marked STRETCH   -> optional extra practice, only after the REQUIRED ones pass.
Each unfinished test calls self.skipTest(...): replace that line with the real test body.
Done when `python manage.py test` shows OK and every skipped test is a STRETCH one (skipped=7 or fewer).
"""
from datetime import timedelta

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Task


class TaskAPITests(APITestCase):
    def setUp(self):
        # ARRANGE - two users, each with a token and one task.
        self.alice = User.objects.create_user(username="alice", password="alice-test-pass-123")
        self.bob = User.objects.create_user(username="bob", password="bob-test-pass-123")
        self.alice_token = Token.objects.create(user=self.alice)
        self.bob_token = Token.objects.create(user=self.bob)

        self.alice_task = Task.objects.create(title="Alice task", owner=self.alice)
        self.bob_task = Task.objects.create(title="Bob task", owner=self.bob)

        # URLs come from the router names: "task-list" and "task-detail".
        self.list_url = reverse("task-list")  # /api/tasks/
        self.alice_detail_url = reverse("task-detail", args=[self.alice_task.id])  # /api/tasks/<id>/
        self.bob_detail_url = reverse("task-detail", args=[self.bob_task.id])
        self.token_url = reverse("api-token")  # /api/auth/token/

    def authenticate(self, token):
        """Send `Authorization: Token <key>` with every following request of this test."""
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    # ------------------------------------------------------------------ authentication

    def test_unauthenticated_request_is_rejected_with_401(self):
        # EXAMPLE (complete) - copy this shape for the other tests.
        response = self.client.get(self.list_url)  # no credentials

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_endpoint_returns_token_for_valid_credentials(self):
        # TODO [Day 4 · P2 · REQUIRED]: POST username + password of alice to self.token_url (format="json").
        #   Assert 200 and that response.data["token"] equals self.alice_token.key
        # HINT: days/day-04/hints.md#p2
        # YOUR CODE HERE
        self.skipTest("REQUIRED - Day 4 · P2: write this test")

    def test_token_endpoint_rejects_wrong_password(self):
        # TODO [Day 4 · P2 · STRETCH (optional)]: POST a wrong password. Assert 400 and that no "token" key is returned.
        # YOUR CODE HERE
        self.skipTest("STRETCH (optional) - Day 4 · P2: write this test")

    # ------------------------------------------------------------------ create + ownership

    def test_create_assigns_owner_from_token(self):
        # TODO [Day 4 · P2 - build together with the instructor · REQUIRED]:
        #   As alice, POST a new task that tries to set "owner": self.bob.id.
        #   Assert 201, response owner is "alice", and the saved Task in the DB belongs to alice.
        # YOUR CODE HERE
        self.skipTest("REQUIRED - Day 4 · P2: write this test")

    def test_list_returns_only_own_tasks(self):
        # TODO [Day 4 · P2 · REQUIRED]: As alice, GET the list. Assert 200 and that only alice's task id is returned.
        # YOUR CODE HERE
        self.skipTest("REQUIRED - Day 4 · P2: write this test")

    # ------------------------------------------------------------------ data isolation

    def test_cannot_retrieve_another_users_task(self):
        # TODO [Day 4 · P2 - build together with the instructor · REQUIRED]:
        #   As alice, GET bob's task. Assert 404 (the task is invisible to alice, not "forbidden").
        # YOUR CODE HERE
        self.skipTest("REQUIRED - Day 4 · P2: write this test")

    def test_cannot_update_another_users_task(self):
        # TODO [Day 4 · P2 · STRETCH (optional)]: As alice, PATCH bob's task title. Assert 404 AND that bob's title is unchanged in the DB.
        #   Remember: call self.bob_task.refresh_from_db() before checking the database value.
        # YOUR CODE HERE
        self.skipTest("STRETCH (optional) - Day 4 · P2: write this test")

    def test_cannot_delete_another_users_task(self):
        # TODO [Day 4 · P2 · STRETCH (optional)]: As alice, DELETE bob's task. Assert 404 AND that bob's task still exists.
        # YOUR CODE HERE
        self.skipTest("STRETCH (optional) - Day 4 · P2: write this test")

    # ------------------------------------------------------------------ CRUD on own tasks

    def test_retrieve_own_task(self):
        # TODO [Day 4 · P2 · STRETCH (optional)]: As alice, GET her task. Assert 200 and the returned title.
        # YOUR CODE HERE
        self.skipTest("STRETCH (optional) - Day 4 · P2: write this test")

    def test_full_update_with_put(self):
        # TODO [Day 4 · P2 · STRETCH (optional)]: As alice, PUT title/description/status/due_date on her task.
        #   Assert 200 and that the DB row now has the new values.
        # YOUR CODE HERE
        self.skipTest("STRETCH (optional) - Day 4 · P2: write this test")

    def test_partial_update_with_patch(self):
        # TODO [Day 4 · P2 · REQUIRED]: As alice, PATCH only {"status": "DONE"}.
        #   Assert 200, status changed, and the title did NOT change.
        # YOUR CODE HERE
        self.skipTest("REQUIRED - Day 4 · P2: write this test")

    def test_delete_own_task(self):
        # TODO [Day 4 · P2 · REQUIRED]: As alice, DELETE her task. Assert 204 and that it is gone from the DB.
        # YOUR CODE HERE
        self.skipTest("REQUIRED - Day 4 · P2: write this test")

    # ------------------------------------------------------------------ validation

    def test_blank_title_is_rejected(self):
        # TODO [Day 4 · P2 · REQUIRED]: As alice, POST {"title": "   "}. Assert 400 and that "title" is in response.data.
        # YOUR CODE HERE
        self.skipTest("REQUIRED - Day 4 · P2: write this test")

    def test_invalid_status_is_rejected(self):
        # TODO [Day 4 · P2 · STRETCH (optional)]: As alice, POST a task with status "FINISHED". Assert 400 with a "status" error.
        # YOUR CODE HERE
        self.skipTest("STRETCH (optional) - Day 4 · P2: write this test")

    def test_past_due_date_is_rejected_on_create(self):
        # TODO [Day 4 · P2 · STRETCH (optional)]: As alice, POST a task whose due_date is yesterday.
        #   Assert 400, a "due_date" error, and that no extra task was saved.
        # YOUR CODE HERE
        self.skipTest("STRETCH (optional) - Day 4 · P2: write this test")
