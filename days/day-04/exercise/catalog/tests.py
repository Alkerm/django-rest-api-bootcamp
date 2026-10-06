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

GOAL: the 4 REQUIRED tests pass (plus the example).  4 STRETCH tests are optional extra practice.
Each test = ARRANGE (setUp) -> ACT (one request) -> ASSERT.
Replace the `self.skipTest(...)` line of a test with the real test body.
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
        # TODO [Day 4 · Task 1-1 · REQUIRED]: POST {"username": "alice", "password": "alice-test-pass"} to "/api/auth/token/".
        #   Expected: 200 and response.data["token"] == self.alice_token.key
        # HINT: days/day-04/hints.md#task-1
        # YOUR CODE HERE - replace the placeholder line below
        self.skipTest("REQUIRED - Day 4 · Task 1: write this test")

    def test_list_shows_only_my_items(self):
        # TODO [Day 4 · Task 1-2 · REQUIRED]: As alice, GET the list.
        #   Expected: 200 and the list contains ONLY alice's item id (bob's item is not there).
        # YOUR CODE HERE - replace the placeholder line below
        self.skipTest("REQUIRED - Day 4 · Task 1: write this test")

    def test_create_sets_user_from_token(self):
        # TODO [Day 4 · Task 1-3 · STRETCH (optional)]: As bob, POST {"book": self.book_1.id, "user": self.alice.id}.
        #   Expected: 201, response "user" is "bob", and the new row in the DATABASE belongs to bob.
        # YOUR CODE HERE - replace the placeholder line below
        self.skipTest("STRETCH (optional) - Day 4 · Task 1: write this test")

    def test_other_users_item_returns_404(self):
        # TODO [Day 4 · Task 1-4 · REQUIRED]: As bob, GET alice's item (self.alice_item_url). Expected: 404.
        # YOUR CODE HERE - replace the placeholder line below
        self.skipTest("REQUIRED - Day 4 · Task 1: write this test")

    def test_other_user_cannot_delete_my_item(self):
        # TODO [Day 4 · Task 1-5 · STRETCH (optional)]: As bob, DELETE alice's item.
        #   Expected: 404 AND alice's item still exists in the database.
        # YOUR CODE HERE - replace the placeholder line below
        self.skipTest("STRETCH (optional) - Day 4 · Task 1: write this test")

    def test_past_target_date_returns_400(self):
        # TODO [Day 4 · Task 1-6 · REQUIRED]: As alice, POST book_2 with target_date = yesterday.
        #   yesterday = timezone.localdate() - timedelta(days=1)   -> send it as yesterday.isoformat()
        #   Expected: 400 and "target_date" in response.data
        # YOUR CODE HERE - replace the placeholder line below
        self.skipTest("REQUIRED - Day 4 · Task 1: write this test")

    def test_duplicate_book_returns_400(self):
        # TODO [Day 4 · Task 1-7 · STRETCH (optional)]: As alice, POST book_1 again (it is already on her list).
        #   Expected: 400, "book" in response.data, and alice still has exactly 1 item in the database.
        # YOUR CODE HERE - replace the placeholder line below
        self.skipTest("STRETCH (optional) - Day 4 · Task 1: write this test")

    def test_patch_updates_only_status(self):
        # TODO [Day 4 · Task 1-8 · STRETCH (optional)]: As alice, PATCH her item with {"status": "FINISHED"}.
        #   Expected: 200; after self.alice_item.refresh_from_db(): status is FINISHED and book is still book_1.
        # YOUR CODE HERE - replace the placeholder line below
        self.skipTest("STRETCH (optional) - Day 4 · Task 1: write this test")
