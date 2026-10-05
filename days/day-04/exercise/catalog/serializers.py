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

    def validate_target_date(self, value):
        if value is not None and value < timezone.localdate():
            raise serializers.ValidationError("Target date cannot be in the past.")
        return value

    def validate_book(self, value):
        user = self.context["request"].user
        duplicates = ReadingListItem.objects.filter(user=user, book=value)
        if self.instance is not None:
            duplicates = duplicates.exclude(pk=self.instance.pk)
        if duplicates.exists():
            raise serializers.ValidationError("This book is already on your reading list.")
        return value
