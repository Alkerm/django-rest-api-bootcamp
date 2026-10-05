"""
Day 3 exercise - ACCEPTANCE CHECKS (given - do not edit).

Run:  python manage.py test
They use a temporary database loaded with the sample data (alice, bob, books, reading-list items),
so they never change your db.sqlite3. When every task is done:  Ran 11 tests ... OK
"""
from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import ReadingListItem


class ReadingListAcceptanceTests(APITestCase):
    fixtures = ["sample_data"]

    def login(self, username, password):
        response = self.client.post(
            "/api/auth/token/", {"username": username, "password": password}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, "token login failed - Task 1")
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response.data['token']}")

    # ---- Task 1: token authentication
    def test_task1_token_login_returns_token(self):
        response = self.client.post(
            "/api/auth/token/", {"username": "alice", "password": "alice-pass-2026"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["token"]), 40)

    def test_task1_wrong_password_returns_400(self):
        response = self.client.post(
            "/api/auth/token/", {"username": "alice", "password": "wrong"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_task1_no_token_returns_401(self):
        self.assertEqual(self.client.get("/api/reading-list/").status_code, status.HTTP_401_UNAUTHORIZED)

    # ---- Task 2: ownership
    def test_task2_alice_sees_only_her_two_items(self):
        self.login("alice", "alice-pass-2026")
        response = self.client.get("/api/reading-list/")
        self.assertEqual([item["id"] for item in response.data], [1, 2])

    def test_task2_bob_cannot_read_change_or_delete_alices_item(self):
        self.login("bob", "bob-pass-2026")
        self.assertEqual(self.client.get("/api/reading-list/1/").status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(
            self.client.patch("/api/reading-list/1/", {"notes": "hacked"}, format="json").status_code,
            status.HTTP_404_NOT_FOUND,
        )
        self.assertEqual(self.client.delete("/api/reading-list/1/").status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(ReadingListItem.objects.get(pk=1).notes, "Chapter 3 next")

    def test_task2_create_sets_user_from_token(self):
        self.login("bob", "bob-pass-2026")
        response = self.client.post("/api/reading-list/", {"book": 1, "user": 1}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"], "bob")
        self.assertEqual(ReadingListItem.objects.get(pk=response.data["id"]).user.username, "bob")

    # ---- Task 3: validation
    def test_task3_past_target_date_returns_400(self):
        self.login("alice", "alice-pass-2026")
        yesterday = (timezone.localdate() - timedelta(days=1)).isoformat()
        response = self.client.post("/api/reading-list/", {"book": 2, "target_date": yesterday}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["target_date"], ["Target date cannot be in the past."])

    def test_task3_today_target_date_is_allowed(self):
        self.login("alice", "alice-pass-2026")
        today = timezone.localdate().isoformat()
        response = self.client.post("/api/reading-list/", {"book": 2, "target_date": today}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_task3_duplicate_book_returns_400(self):
        self.login("alice", "alice-pass-2026")
        response = self.client.post("/api/reading-list/", {"book": 1}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["book"], ["This book is already on your reading list."])

    def test_task3_same_book_for_another_user_is_allowed(self):
        self.login("bob", "bob-pass-2026")
        response = self.client.post("/api/reading-list/", {"book": 1}, format="json")  # alice has it, bob does not
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_task3_updating_an_item_keeps_its_own_book(self):
        self.login("alice", "alice-pass-2026")
        response = self.client.put(
            "/api/reading-list/1/", {"book": 1, "status": "FINISHED", "notes": "Done!"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
