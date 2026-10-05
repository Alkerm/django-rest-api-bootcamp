"""
Day 4 exercise - Task 1: automated tests for the reading-list API.

BEFORE YOU START
    * No database setup is needed for tests: `python manage.py test` creates a temporary EMPTY test database,
      runs setUp() before EVERY test, and deletes the database afterwards. Your db.sqlite3 is never touched.
    * The sample data fixture is NOT used here. setUp() creates exactly the data each test needs (listed below).
    * Run:  python manage.py test            (all tests)
            python manage.py test -v 2       (show each test name)

DATA CREATED BY setUp() (fresh for every test)
    users            alice (password "alice-test-pass")   bob (password "bob-test-pass")
    tokens           self.alice_token, self.bob_token
    books            self.book_1 "Clean Code" (id varies!)   self.book_2 "Refactoring"
    reading list     self.alice_item -> alice + book_1, status READING
                     self.bob_item   -> bob   + book_2, status WANT_TO_READ
    Never hard-code ids like 1 or 2: use self.alice_item.id, self.book_2.id, ...

GOAL: at least 8 passing tests and "skipped=0". Each test = ARRANGE (setUp) -> ACT (one request) -> ASSERT.
Replace every `self.skipTest(...)` line with the real test.
"""
from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Author, Book, ReadingListItem


class ReadingListAPITests(APITestCase):
    def setUp(self):
        # GIVEN - test data (see the docstring above)
        self.alice = User.objects.create_user(username="alice", password="alice-test-pass")
        self.bob = User.objects.create_user(username="bob", password="bob-test-pass")
        self.alice_token = Token.objects.create(user=self.alice)
        self.bob_token = Token.objects.create(user=self.bob)

        author = Author.objects.create(name="Test Author")
        self.book_1 = Book.objects.create(title="Clean Code", isbn="1000000000001", published_year=2008, author=author)
        self.book_2 = Book.objects.create(title="Refactoring", isbn="1000000000002", published_year=1999, author=author)

        self.alice_item = ReadingListItem.objects.create(user=self.alice, book=self.book_1, status="READING")
        self.bob_item = ReadingListItem.objects.create(user=self.bob, book=self.book_2)

        self.list_url = "/api/reading-list/"
        self.alice_item_url = f"/api/reading-list/{self.alice_item.id}/"

    def use_token(self, token):
        """GIVEN - send 'Authorization: Token <key>' with every following request in this test."""
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    # ------------------------------------------------------------------ EXAMPLE (complete)
    def test_no_token_returns_401(self):
        # ACT: request without credentials
        response = self.client.get(self.list_url)
        # ASSERT: rejected, and the response explains why
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response.data)

    # ------------------------------------------------------------------ YOUR TESTS
    def test_token_login_returns_token(self):
        response = self.client.post(
            "/api/auth/token/", {"username": "alice", "password": "alice-test-pass"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["token"], self.alice_token.key)

    def test_list_shows_only_my_items(self):
        self.use_token(self.alice_token)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([item["id"] for item in response.data], [self.alice_item.id])

    def test_create_sets_user_from_token(self):
        self.use_token(self.bob_token)
        response = self.client.post(self.list_url, {"book": self.book_1.id, "user": self.alice.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"], "bob")
        self.assertEqual(ReadingListItem.objects.get(id=response.data["id"]).user, self.bob)

    def test_other_users_item_returns_404(self):
        self.use_token(self.bob_token)
        response = self.client.get(self.alice_item_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_other_user_cannot_delete_my_item(self):
        self.use_token(self.bob_token)
        response = self.client.delete(self.alice_item_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue(ReadingListItem.objects.filter(id=self.alice_item.id).exists())

    def test_past_target_date_returns_400(self):
        self.use_token(self.alice_token)
        yesterday = timezone.localdate() - timedelta(days=1)
        response = self.client.post(
            self.list_url, {"book": self.book_2.id, "target_date": yesterday.isoformat()}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("target_date", response.data)

    def test_duplicate_book_returns_400(self):
        self.use_token(self.alice_token)
        response = self.client.post(self.list_url, {"book": self.book_1.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("book", response.data)
        self.assertEqual(ReadingListItem.objects.filter(user=self.alice).count(), 1)

    def test_patch_updates_only_status(self):
        self.use_token(self.alice_token)
        response = self.client.patch(self.alice_item_url, {"status": "FINISHED"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.alice_item.refresh_from_db()
        self.assertEqual(self.alice_item.status, "FINISHED")
        self.assertEqual(self.alice_item.book, self.book_1)
