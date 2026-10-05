"""
Day 2 exercise - Task 1: serializers (model <-> JSON, plus input validation).
"""
from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """GIVEN - a complete example. Copy its shape for BookSerializer."""

    class Meta:
        model = Author
        fields = ["id", "name", "country"]
        read_only_fields = ["id"]


class BookSerializer(serializers.ModelSerializer):
    """
    JSON shape the API must return for one book:
        {
          "id": 1,
          "title": "Clean Code",
          "isbn": "9780000000011",
          "published_year": 2008,
          "available_copies": 3,
          "author": 1,                       <- writable: the client sends the author's id
          "author_name": "Robert C. Martin",  <- read-only: comes from book.author.name
          "created_at": "2026-10-01T12:01:00+03:00"
        }
    """

    # TODO [Day 2 · Task 1a]: Declare the extra read-only field `author_name` whose source is "author.name".
    # HINT: days/day-02/hints.md#task-1  |  Example: days/day-02/example/serializers.py
    # YOUR CODE HERE

    class Meta:
        model = Book
        # TODO [Day 2 · Task 1b]: List all 8 fields in the order shown above,
        #   and make `id` and `created_at` read-only (the server sets them).
        # YOUR CODE HERE
        fields = ["id"]
