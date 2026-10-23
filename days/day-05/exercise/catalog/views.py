"""
Day 5 exercise - the finished reading-list API from Day 4 (GIVEN - today you change configuration only).

Every view here requires a logged-in user (DEFAULT_PERMISSION_CLASSES = IsAuthenticated in settings):
    no or invalid token -> 401 before the view even runs.
Inside the view, request.user is the user the token belongs to.
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book, ReadingListItem
from .serializers import BookSerializer, ReadingListItemSerializer


# ------------------------------------------------------------------ GIVEN: the shared book catalog (read-only)
@api_view(["GET"])
def list_books(request):
    """GIVEN - any authenticated user may browse the catalog."""
    books = Book.objects.select_related("author")
    return Response(BookSerializer(books, many=True).data)


@api_view(["GET"])
def get_book(request, pk):
    """GIVEN"""
    return Response(BookSerializer(get_object_or_404(Book, pk=pk)).data)


# ------------------------------------------------------------------ MY reading list
@api_view(["GET"])
def list_items(request):
    """GET /api/reading-list/  ->  only MY items."""
    items = ReadingListItem.objects.filter(user=request.user).select_related("book")
    return Response(ReadingListItemSerializer(items, many=True).data)


def get_own_item(request, pk):
    """Find ONE item by id - but only among the caller's own items. Used by get, update and delete below."""
    return get_object_or_404(ReadingListItem, pk=pk, user=request.user)


@api_view(["POST"])
def create_item(request):
    """POST /api/reading-list/create/  ->  the new item belongs to the caller."""
    # context={"request": request}: the serializer's validate_book() needs to know who is asking (Task 3b).
    serializer = ReadingListItemSerializer(data=request.data, context={"request": request})
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save(user=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_item(request, pk):
    """GIVEN - GET /api/reading-list/<pk>/"""
    return Response(ReadingListItemSerializer(get_own_item(request, pk)).data)


@api_view(["PUT", "PATCH"])
def update_item(request, pk):
    """GIVEN - PUT/PATCH /api/reading-list/<pk>/update/"""
    item = get_own_item(request, pk)
    serializer = ReadingListItemSerializer(
        item, data=request.data, partial=request.method == "PATCH", context={"request": request}
    )
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_item(request, pk):
    """GIVEN - DELETE /api/reading-list/<pk>/delete/"""
    get_own_item(request, pk).delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
