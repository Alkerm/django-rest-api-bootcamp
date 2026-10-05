"""
Day 3 exercise - Task 3: validation rules for the reading list.
"""
from django.utils import timezone
from rest_framework import serializers

from .models import Book, ReadingListItem


class BookSerializer(serializers.ModelSerializer):
    """GIVEN - read-only book catalog."""

    author_name = serializers.ReadOnlyField(source="author.name")

    class Meta:
        model = Book
        fields = ["id", "title", "isbn", "published_year", "available_copies", "author", "author_name"]


class ReadingListItemSerializer(serializers.ModelSerializer):
    """
    GIVEN - fields and read-only parts. JSON shape:
        {"id": 1, "user": "alice", "book": 1, "book_title": "Clean Code",
         "status": "READING", "target_date": "2026-12-31", "notes": "Chapter 3 next", "created_at": "..."}
    `user` is read-only: the view sets it from the token (Task 2).
    """

    user = serializers.ReadOnlyField(source="user.username")
    book_title = serializers.ReadOnlyField(source="book.title")

    class Meta:
        model = ReadingListItem
        fields = ["id", "user", "book", "book_title", "status", "target_date", "notes", "created_at"]
        read_only_fields = ["id", "created_at"]
        # The (user, book) uniqueness is checked in validate_book() below - that gives a clear field error.
        validators = []

    # TODO [Day 3 · Task 3a]: Reject a target_date in the past.
    #   - Method name: validate_target_date(self, value)
    #   - None (no date) is allowed. Today is allowed. Yesterday is not.
    #   - "Today" = timezone.localdate()
    #   - Error message: "Target date cannot be in the past."
    # HINT: days/day-03/hints.md#task-3  |  Example: days/day-03/example/serializers.py
    # YOUR CODE HERE

    # TODO [Day 3 · Task 3b]: Reject a book that is ALREADY on the current user's reading list.
    #   - Method name: validate_book(self, value)          (value is a Book instance)
    #   - The current user: self.context["request"].user   (DRF passes the request to the serializer)
    #   - When UPDATING (self.instance is not None), exclude the item being edited: .exclude(pk=self.instance.pk)
    #   - Error message: "This book is already on your reading list."
    # HINT: days/day-03/hints.md#task-3
    # YOUR CODE HERE
