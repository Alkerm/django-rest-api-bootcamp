"""
Day 3 exercise - Task 1 (BookSerializer) and Task 3 (validation).

A serializer is a TRANSLATOR (model <-> JSON) and a GATEKEEPER (rejects invalid input before saving).
It replaces yesterday's book_to_dict() AND the hand-written REQUIRED_FIELDS checks.
"""
from django.utils import timezone
from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """GIVEN - the complete pattern. Compare it with yesterday's author_to_dict()."""

    class Meta:
        model = Author
        fields = ["id", "name", "country"]
        read_only_fields = ["id"]


class BookSerializer(serializers.ModelSerializer):
    """
    JSON shape (8 fields, in this order):
        id, title, isbn, published_year, available_copies, author, author_name, created_at

    - author       -> writable: the client sends the author's id, e.g. 2
    - author_name  -> READ-ONLY, not a column: comes from book.author.name
    - id, created_at -> read-only: the server sets them
    """

    # TODO [Day 3 · Task 1a]: Declare author_name as a read-only field whose value comes from book.author.name.
    # HINT: days/day-03/hints.md#task-1  |  Example: days/day-03/example/serializers.py (director_name)
    # YOUR CODE HERE

    class Meta:
        model = Book
        # TODO [Day 3 · Task 1b]: List the 8 fields (in the order above) and mark id and created_at as read-only.
        # HINT: days/day-03/hints.md#task-1
        # YOUR CODE HERE - replace the placeholder line below
        fields = ["id"]
        # TODO [Day 3 · Task 3a]: Give a blank title this exact message: "Title cannot be blank."
        #   (DRF already rejects a blank title; you only change the TEXT, with extra_kwargs.)
        # HINT: days/day-03/hints.md#task-3
        # YOUR CODE HERE

    # TODO [Day 3 · Task 3b]: Reject a published_year later than the current year (this year is fine).
    #   Message: "Published year cannot be in the future."   Tip: timezone.localdate().year
    # HINT: days/day-03/hints.md#task-3  |  Example: days/day-03/example/serializers.py (validate_release_date)
    # YOUR CODE HERE

    # TODO [Day 3 · Task 4 · STRETCH (optional)]: An author cannot have two books with the same title.
    #   Object-level rule: def validate(self, attrs). On create, title and author are in attrs; on PATCH one of
    #   them may be missing -> fall back to self.instance. Exclude the book itself when updating.
    #   Message (non-field error): "This author already has a book with this title."
    # HINT: days/day-03/hints.md#task-4  |  Example: days/day-03/example/serializers.py (validate)
    # YOUR CODE HERE
