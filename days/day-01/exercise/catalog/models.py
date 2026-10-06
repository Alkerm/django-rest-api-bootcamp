"""
Day 1 exercise - Task 1: complete the Book model.

BEFORE YOU START (run inside days/day-01/exercise with your .venv active):
    python manage.py check          -> should print "System check identified no issues"
The database does NOT exist yet and holds no data. You create it in Task 2.
"""
from django.db import models


class Author(models.Model):
    """GIVEN - use it as a model to copy from.  Table: catalog_author"""

    name = models.CharField(max_length=120)
    country = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    """One book in the library.  Table: catalog_book"""

    # GIVEN - the relationship: many books -> one author.  author.books.all() lists an author's books.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    # TODO [Day 1 · Task 1]: Add the four Book fields below.
    #   field             Django type                        rules
    #   title             CharField                          max_length=200
    #   isbn              CharField                          max_length=13, unique=True   (no two books share an ISBN)
    #   published_year    PositiveIntegerField               required (whole number >= 0)
    #   available_copies  PositiveIntegerField               default=1
    # HINT: days/day-01/hints.md#task-1  |  Example: days/day-01/example/models.py
    # YOUR CODE HERE

    def __str__(self):
        # TODO [Day 1 · Task 1]: Return the book title so the admin shows "Clean Code" instead of "Book object (1)".
        # YOUR CODE HERE - replace the placeholder line below
        return super().__str__()
