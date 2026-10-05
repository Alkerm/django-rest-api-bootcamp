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

    def get_queryset(self):
        return ReadingListItem.objects.filter(user=self.request.user).select_related("book")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
