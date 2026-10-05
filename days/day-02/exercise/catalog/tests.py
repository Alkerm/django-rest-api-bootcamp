"""
Day 2 exercise - ACCEPTANCE CHECKS (given - do not edit).

Run:  python manage.py test
These tests build their own temporary database with the sample data, so they never change your db.sqlite3.
When every task is done you should see:  Ran 9 tests ... OK
"""
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book


class BookAPIAcceptanceTests(APITestCase):
    fixtures = ["sample_data"]

    def test_task1_book_json_has_all_fields(self):
        response = self.client.get("/api/books/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            list(response.data.keys()),
            ["id", "title", "isbn", "published_year", "available_copies", "author", "author_name", "created_at"],
        )
        self.assertEqual(response.data["author_name"], "Robert C. Martin")

    def test_task2_list_returns_all_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    def test_task2_create_returns_201_and_saves_row(self):
        payload = {"title": "Domain-Driven Design", "isbn": "9780000000073", "published_year": 2003,
                   "available_copies": 2, "author": 2}
        response = self.client.post("/api/books/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["id"], 7)
        self.assertTrue(Book.objects.filter(isbn="9780000000073").exists())

    def test_task2_server_controls_read_only_fields(self):
        payload = {"id": 99, "title": "Read-only check", "isbn": "9780000000080", "published_year": 2020,
                   "author": 1, "created_at": "2000-01-01T00:00:00Z"}
        response = self.client.post("/api/books/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data["id"], 99)
        self.assertFalse(response.data["created_at"].startswith("2000"))

    def test_task2_invalid_input_returns_400(self):
        payload = {"title": "", "isbn": "9780000000011", "published_year": -5, "author": 999}
        response = self.client.post("/api/books/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        for field in ["title", "isbn", "published_year", "author"]:
            self.assertIn(field, response.data)

    def test_task2_put_replaces_book(self):
        payload = {"title": "Clean Code (2nd ed.)", "isbn": "9780000000011", "published_year": 2025,
                   "available_copies": 5, "author": 1}
        response = self.client.put("/api/books/1/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=1).published_year, 2025)

    def test_task2_patch_changes_only_given_field(self):
        response = self.client.patch("/api/books/2/", {"available_copies": 7}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = Book.objects.get(pk=2)
        self.assertEqual(book.available_copies, 7)
        self.assertEqual(book.title, "The Clean Coder")

    def test_task2_delete_returns_204_then_404(self):
        self.assertEqual(self.client.delete("/api/books/6/").status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.client.get("/api/books/6/").status_code, status.HTTP_404_NOT_FOUND)

    def test_task3_books_are_listed_a_to_z(self):
        response = self.client.get("/api/books/")
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles))
