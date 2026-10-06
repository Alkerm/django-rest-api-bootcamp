"""
Day 2 exercise - ACCEPTANCE CHECKS (given - do not edit).

Run:  python manage.py test             (all tasks)
      python manage.py test -k task1    (only Task 1, works before Task 2 exists)
These tests build their own temporary database with the sample data, so they never change your db.sqlite3.
Before you start, they fail - that is expected. They turn green task by task.
Core (Tasks 1-3):     python manage.py test -k task1 -k task2 -k task3   ->  Ran 11 tests ... OK
With stretch Task 4:  python manage.py test                                 ->  Ran 12 tests ... OK
"""
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book
from .serializers import BookSerializer

NO_ROUTE = "GET /api/books/... returned 404: is BookViewSet registered on the router as 'books'? (Task 2)"


class BookAPIAcceptanceTests(APITestCase):
    fixtures = ["sample_data"]

    def test_task1_book_json_has_all_fields(self):
        data = BookSerializer(Book.objects.get(pk=1)).data
        self.assertEqual(
            list(data.keys()),
            ["id", "title", "isbn", "published_year", "available_copies", "author", "author_name", "created_at"],
            "BookSerializer must list exactly these 8 fields, in this order (Task 1b)",
        )
        self.assertEqual(data["author_name"], "Robert C. Martin",
                         "author_name should come from book.author.name (Task 1a)")

    def test_task2_list_returns_all_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK, NO_ROUTE)
        self.assertEqual(len(response.data), 6, "the list should contain all 6 sample books")

    def test_task2_create_returns_201_and_saves_row(self):
        payload = {"title": "Domain-Driven Design", "isbn": "9780000000073", "published_year": 2003,
                   "available_copies": 2, "author": 2}
        response = self.client.post("/api/books/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         f"POST /api/books/ should create the book (201). Response: {response.data}")
        self.assertEqual(response.data["id"], 7)
        self.assertTrue(Book.objects.filter(isbn="9780000000073").exists(), "the new row was not saved")

    def test_task2_server_controls_read_only_fields(self):
        payload = {"id": 99, "title": "Read-only check", "isbn": "9780000000080", "published_year": 2020,
                   "author": 1, "created_at": "2000-01-01T00:00:00Z"}
        response = self.client.post("/api/books/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, NO_ROUTE)
        self.assertNotEqual(response.data["id"], 99, "the client must not choose the id (read_only_fields, Task 1b)")
        self.assertFalse(response.data["created_at"].startswith("2000"),
                         "the client must not set created_at (read_only_fields, Task 1b)")

    def test_task2_invalid_input_returns_400(self):
        payload = {"title": "", "isbn": "9780000000011", "published_year": -5, "author": 999}
        response = self.client.post("/api/books/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, NO_ROUTE)
        for field in ["title", "isbn", "published_year", "author"]:
            self.assertIn(field, response.data, f"expected a validation error for '{field}'")

    def test_task2_put_replaces_book(self):
        payload = {"title": "Clean Code (2nd ed.)", "isbn": "9780000000011", "published_year": 2025,
                   "available_copies": 5, "author": 1}
        response = self.client.put("/api/books/1/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, NO_ROUTE)
        self.assertEqual(Book.objects.get(pk=1).published_year, 2025, "PUT did not update the database row")

    def test_task2_patch_changes_only_given_field(self):
        response = self.client.patch("/api/books/2/", {"available_copies": 7}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, NO_ROUTE)
        book = Book.objects.get(pk=2)
        self.assertEqual(book.available_copies, 7, "PATCH did not update available_copies")
        self.assertEqual(book.title, "The Clean Coder", "PATCH must not change fields that were not sent")

    def test_task2_delete_returns_204_then_404(self):
        self.assertEqual(self.client.delete("/api/books/6/").status_code, status.HTTP_204_NO_CONTENT, NO_ROUTE)
        self.assertEqual(self.client.get("/api/books/6/").status_code, status.HTTP_404_NOT_FOUND,
                         "after DELETE the book should be gone")

    def test_task3_blank_title_has_clear_message(self):
        payload = {"title": "   ", "isbn": "9780000000097", "published_year": 2020, "author": 1}
        response = self.client.post("/api/books/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, NO_ROUTE)
        self.assertEqual(response.data.get("title"), ["Title cannot be blank."],
                         "add extra_kwargs with the blank-title message (Task 3a)")

    def test_task3_future_year_is_rejected(self):
        next_year = timezone.localdate().year + 1
        payload = {"title": "From the future", "isbn": "9780000000103", "published_year": next_year, "author": 1}
        response = self.client.post("/api/books/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,
                         "a future published_year must be rejected: add validate_published_year() (Task 3b)")
        self.assertEqual(response.data.get("published_year"), ["Published year cannot be in the future."])

    def test_task3_this_year_is_allowed(self):
        payload = {"title": "Brand new", "isbn": "9780000000110", "published_year": timezone.localdate().year, "author": 1}
        response = self.client.post("/api/books/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         f"this year must be allowed (use '>' not '>='). Response: {response.data}")

    def test_task4_books_are_listed_a_to_z(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK, NO_ROUTE)
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles),
                         "books are not sorted A-Z: add Meta.ordering = ['title'] and run makemigrations + migrate (stretch Task 4)")
