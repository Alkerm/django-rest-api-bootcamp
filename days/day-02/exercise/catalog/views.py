"""
Day 2 exercise - function views: one function per CRUD operation (no serializer yet, that is Day 3).

Every view follows the same three steps:
    1. @api_view([...])  -> which HTTP methods are allowed (others get 405); the JSON body arrives in request.data
    2. ORM               -> read or change rows (Day 1)
    3. Response(...)     -> a dict or a list of dicts, plus a status code; DRF turns it into JSON
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Author, Book


# ------------------------------------------------------------------ GIVEN: the complete pattern for authors
def author_to_dict(author):
    """GIVEN - one Author row -> a plain dict. You choose the keys and their order."""
    return {
        "id": author.id,
        "name": author.name,
        "country": author.country,
    }


@api_view(["GET"])
def list_authors(request):
    """GIVEN - GET /api/authors/  ->  200 + a list of every author."""
    authors = Author.objects.all()
    return Response([author_to_dict(author) for author in authors])


# ------------------------------------------------------------------ Task 1: object -> dict
def book_to_dict(book):
    # TODO [Day 2 · Task 1]: Return a dict with these 8 keys, in this order:
    #   id, title, isbn, published_year, available_copies, author, author_name, created_at
    #   - "author"      -> the author's id   (book.author_id)
    #   - "author_name" -> the author's name (book.author.name), a value that is not a column of catalog_book
    # HINT: days/day-02/hints.md#task-1  |  Example: days/day-02/example/views.py (movie_to_dict)
    # YOUR CODE HERE - replace the placeholder line below
    return {"id": book.id}


# ------------------------------------------------------------------ Task 2: list + create
@api_view(["GET"])
def list_books(request):
    """GET /api/books/  ->  200 + a list of every book."""
    # TODO [Day 2 · Task 2a]: Query every book and return them as a list of dicts (use book_to_dict).
    #   Look at list_authors above: it is the same pattern.
    # HINT: days/day-02/hints.md#task-2
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


REQUIRED_FIELDS = ["title", "isbn", "published_year", "author"]   # GIVEN - used by create_book


@api_view(["POST"])
def create_book(request):
    """POST /api/books/create/  ->  201 + the new book, or 400 when a required field is missing."""
    # TODO [Day 2 · Task 2b]: Create a book from request.data.
    #   1. For every name in REQUIRED_FIELDS that is missing or empty in request.data, collect an error:
    #        {"title": ["This field is required."], ...}  -> if there is any, return it with status 400.
    #   2. Find the author: get_object_or_404(Author, pk=request.data["author"])   (unknown id -> 404)
    #   3. Book.objects.create(...) with title, isbn, published_year, author, and available_copies
    #      (optional: request.data.get("available_copies", 1)). Never take id or created_at from the client.
    #   4. Return the new book as a dict with status 201.
    # HINT: days/day-02/hints.md#task-2  |  Example: days/day-02/example/views.py (create_movie)
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


# ------------------------------------------------------------------ Task 3: retrieve, update, delete
@api_view(["GET"])
def get_book(request, pk):
    """GET /api/books/<pk>/  ->  200 + one book, or 404 for an unknown id."""
    # TODO [Day 2 · Task 3a]: Find the book with this pk (unknown id -> 404) and return it as a dict.
    # HINT: days/day-02/hints.md#task-3
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


UPDATABLE_FIELDS = ["title", "isbn", "published_year", "available_copies"]   # GIVEN - used by update_book


@api_view(["PUT", "PATCH"])
def update_book(request, pk):
    """PUT or PATCH /api/books/<pk>/update/  ->  200 + the changed book (404 for an unknown id)."""
    # TODO [Day 2 · Task 3b]: Change ONLY the fields that were sent.
    #   1. Find the book (unknown id -> 404).
    #   2. For every name in UPDATABLE_FIELDS that is in request.data: setattr(book, name, request.data[name])
    #   3. If "author" was sent: book.author = get_object_or_404(Author, pk=request.data["author"])
    #   4. book.save(), then return the book as a dict (200).
    # HINT: days/day-02/hints.md#task-3
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["DELETE"])
def delete_book(request, pk):
    """DELETE /api/books/<pk>/delete/  ->  204 with an empty body (404 for an unknown id)."""
    # TODO [Day 2 · Task 3c]: Find the book (unknown id -> 404), delete it, return status 204 and no data.
    # HINT: days/day-02/hints.md#task-3
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
