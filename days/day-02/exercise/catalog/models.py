"""
Day 2 exercise - the models are GIVEN (you built them yesterday).

Table catalog_author: id, name, country
Table catalog_book:   id, title, isbn (unique), published_year, available_copies, author_id -> catalog_author, created_at
"""
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    published_year = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    # TODO [Day 2 · Task 4 · STRETCH (optional) - Day 1 review]: Sort books A-Z by title in every list.
    #   Add an inner Meta class with ordering = ["title"], then run makemigrations + migrate.
    # HINT: days/day-02/hints.md#task-4
    # YOUR CODE HERE

    def __str__(self):
        return self.title
