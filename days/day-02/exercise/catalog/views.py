"""
Day 2 exercise - Task 2: viewsets (request -> queryset/serializer -> response).
"""
from rest_framework import viewsets

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """GIVEN - read-only: list + retrieve only.  GET /api/authors/  and  GET /api/authors/{id}/"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# TODO [Day 2 · Task 2a]: Create BookViewSet with FULL CRUD (all six operations).
#   - Which base class gives list, create, retrieve, update, partial_update AND destroy?
#   - queryset         -> every book
#   - serializer_class -> BookSerializer
# HINT: days/day-02/hints.md#task-2  |  Example: days/day-02/example/views.py
# YOUR CODE HERE - replace the placeholder lines below
class BookViewSet(viewsets.GenericViewSet):
    pass
