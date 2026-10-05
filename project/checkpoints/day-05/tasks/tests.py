"""
Automated API tests for the Task Management API.

Run them with:   python manage.py test
Each test is an executable promise:  ARRANGE known data -> ACT (one request) -> ASSERT status + body + database.

The test runner builds a brand-new, empty test database for every run, so these tests never touch
your db.sqlite3 data, and each test starts from the same setUp() state (order does not matter).

Requirement: at least 8 meaningful tests pass, none of the required ones skipped.
In your starting file one test is complete (the example). Every other test calls self.skipTest(...):
replace that line with the real test body. `python manage.py test` shows "skipped=N" until you are done.
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
        response = self.client.post(
            self.token_url,
            {"username": "alice", "password": "alice-test-pass-123"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["token"], self.alice_token.key)

    def test_token_endpoint_rejects_wrong_password(self):
        response = self.client.post(
            self.token_url,
            {"username": "alice", "password": "wrong-password"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", response.data)

    # ------------------------------------------------------------------ create + ownership

    def test_create_assigns_owner_from_token(self):
        self.authenticate(self.alice_token)

        response = self.client.post(
            self.list_url,
            {"title": "New task", "owner": self.bob.id},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["owner"], "alice")
        self.assertEqual(Task.objects.get(id=response.data["id"]).owner, self.alice)

    def test_list_returns_only_own_tasks(self):
        self.authenticate(self.alice_token)

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        returned_ids = [task["id"] for task in response.data]
        self.assertEqual(returned_ids, [self.alice_task.id])

    # ------------------------------------------------------------------ data isolation

    def test_cannot_retrieve_another_users_task(self):
        self.authenticate(self.alice_token)

        response = self.client.get(self.bob_detail_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_cannot_update_another_users_task(self):
        self.authenticate(self.alice_token)

        response = self.client.patch(self.bob_detail_url, {"title": "Hacked"}, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.bob_task.refresh_from_db()
        self.assertEqual(self.bob_task.title, "Bob task")

    def test_cannot_delete_another_users_task(self):
        self.authenticate(self.alice_token)

        response = self.client.delete(self.bob_detail_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue(Task.objects.filter(id=self.bob_task.id).exists())

    # ------------------------------------------------------------------ CRUD on own tasks

    def test_retrieve_own_task(self):
        self.authenticate(self.alice_token)

        response = self.client.get(self.alice_detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Alice task")

    def test_full_update_with_put(self):
        self.authenticate(self.alice_token)
        tomorrow = timezone.localdate() + timedelta(days=1)

        response = self.client.put(
            self.alice_detail_url,
            {
                "title": "Updated title",
                "description": "Updated description",
                "status": Task.Status.IN_PROGRESS,
                "due_date": tomorrow.isoformat(),
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.alice_task.refresh_from_db()
        self.assertEqual(self.alice_task.title, "Updated title")
        self.assertEqual(self.alice_task.status, Task.Status.IN_PROGRESS)
        self.assertEqual(self.alice_task.due_date, tomorrow)

    def test_partial_update_with_patch(self):
        self.authenticate(self.alice_token)

        response = self.client.patch(self.alice_detail_url, {"status": "DONE"}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.alice_task.refresh_from_db()
        self.assertEqual(self.alice_task.status, Task.Status.DONE)
        self.assertEqual(self.alice_task.title, "Alice task")

    def test_delete_own_task(self):
        self.authenticate(self.alice_token)

        response = self.client.delete(self.alice_detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.alice_task.id).exists())

    # ------------------------------------------------------------------ validation

    def test_blank_title_is_rejected(self):
        self.authenticate(self.alice_token)

        response = self.client.post(self.list_url, {"title": "   "}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)

    def test_invalid_status_is_rejected(self):
        self.authenticate(self.alice_token)

        response = self.client.post(
            self.list_url, {"title": "Task", "status": "FINISHED"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("status", response.data)

    def test_past_due_date_is_rejected_on_create(self):
        self.authenticate(self.alice_token)
        yesterday = timezone.localdate() - timedelta(days=1)

        response = self.client.post(
            self.list_url,
            {"title": "Late task", "due_date": yesterday.isoformat()},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("due_date", response.data)
        self.assertEqual(Task.objects.filter(owner=self.alice).count(), 1)
