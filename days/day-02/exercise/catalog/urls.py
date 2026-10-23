"""
Day 2 exercise - Task 4: plain path() routing, one URL per view function.

    path(<url pattern>, <view function>, name=<url name>)

These routes are mounted under /api/ in config/urls.py (GIVEN), so "books/" becomes /api/books/.
"""
from django.urls import path

from . import views

urlpatterns = [
    path("authors/", views.list_authors, name="author-list"),  # GIVEN
    # TODO [Day 2 · Task 4]: Add one path() per book view, with exactly these URLs and names:
    #   books/                    views.list_books    name="book-list"
    #   books/create/             views.create_book   name="book-create"
    #   books/<int:pk>/           views.get_book      name="book-detail"
    #   books/<int:pk>/update/    views.update_book   name="book-update"
    #   books/<int:pk>/delete/    views.delete_book   name="book-delete"
    # HINT: days/day-02/hints.md#task-4  |  Example: days/day-02/example/urls.py
    # YOUR CODE HERE
]
