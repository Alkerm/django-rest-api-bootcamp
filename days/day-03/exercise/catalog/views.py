"""
Day 3 exercise - Task 2: the same five function views as yesterday, now with a serializer.

    OUTPUT:  BookSerializer(book).data                  -> one dict
             BookSerializer(books, many=True).data      -> a list of dicts
    INPUT:   serializer = BookSerializer(data=request.data)
             serializer.is_valid()  -> False: serializer.errors = {"field": ["message"]}  -> 400
                                    -> True:  serializer.save() creates the row          -> 201
    UPDATE:  BookSerializer(book, data=request.data, partial=...)   PUT: every field   PATCH: only some
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


@api_view(["GET"])
def list_authors(request):
    """GIVEN - the complete pattern: queryset -> serializer(many=True) -> .data"""
    authors = Author.objects.all()
    return Response(AuthorSerializer(authors, many=True).data)


@api_view(["GET"])
def list_books(request):
    # TODO [Day 3 · Task 2a]: Return every book through BookSerializer (many=True).
    # HINT: days/day-03/hints.md#task-2
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["GET"])
def get_book(request, pk):
    # TODO [Day 3 · Task 2b]: Return one book through BookSerializer (unknown id -> 404).
    # HINT: days/day-03/hints.md#task-2
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["POST"])
def create_book(request):
    # TODO [Day 3 · Task 2c]: Validate request.data with BookSerializer.
    #   invalid -> 400 with serializer.errors (nothing saved)
    #   valid   -> serializer.save(), then 201 with serializer.data
    # HINT: days/day-03/hints.md#task-2  |  Example: days/day-03/example/views.py (create_movie)
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["PUT", "PATCH"])
def update_book(request, pk):
    # TODO [Day 3 · Task 2d]: Update the book through BookSerializer.
    #   - Pass the existing book AND the new data: BookSerializer(book, data=request.data, partial=...)
    #   - partial must be True for PATCH (some fields) and False for PUT (every required field).
    #   - invalid -> 400 with serializer.errors;  valid -> save, 200 with serializer.data
    # HINT: days/day-03/hints.md#task-2
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["DELETE"])
def delete_book(request, pk):
    """GIVEN - delete needs no serializer: nothing is read or written as JSON."""
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
