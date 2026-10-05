"""
Day 3 exercise - Task 2: ownership (each user only sees and changes their own reading list).
"""
from rest_framework import viewsets

from .models import Book, ReadingListItem
from .serializers import BookSerializer, ReadingListItemSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """GIVEN - any authenticated user may browse the catalog: GET /api/books/ and /api/books/{id}/"""

    queryset = Book.objects.select_related("author")
    serializer_class = BookSerializer


class ReadingListItemViewSet(viewsets.ModelViewSet):
    """Full CRUD on MY reading list: /api/reading-list/ and /api/reading-list/{id}/"""

    serializer_class = ReadingListItemSerializer

    # TODO [Day 3 · Task 2a]: Return ONLY the reading-list items of the user who sent the request.
    #   The stub below returns everyone's items -> alice can see bob's list. Fix it with get_queryset().
    # HINT: days/day-03/hints.md#task-2  |  Example: days/day-03/example/views.py
    # YOUR CODE HERE
    queryset = ReadingListItem.objects.all()

    # TODO [Day 3 · Task 2b]: Save new items with user = the user who sent the request.
    #   Without this, creating an item fails with an IntegrityError (user_id cannot be NULL).
    # HINT: days/day-03/hints.md#task-2
    # YOUR CODE HERE
