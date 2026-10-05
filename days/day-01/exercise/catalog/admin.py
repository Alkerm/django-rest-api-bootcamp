"""
Day 1 exercise - Task 3A: show the library in the Django admin.
"""
from django.contrib import admin

from .models import Author, Book


# GIVEN - Author is registered with a customised list page. Copy this pattern for Book.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "country"]
    search_fields = ["name"]


# TODO [Day 1 · Task 3A]: Register Book with a BookAdmin class:
#   list_display  -> id, title, author, published_year, available_copies
#   list_filter   -> author
#   search_fields -> title, isbn
# HINT: days/day-01/hints.md#task-3  |  Example: days/day-01/example/admin.py
# YOUR CODE HERE
