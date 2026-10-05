"""
Day 3 exercise - the models are GIVEN.

Table catalog_author:            id, name, country
Table catalog_book:              id, title, isbn, published_year, available_copies, author_id, created_at
Table catalog_readinglistitem:   id, user_id -> auth_user, book_id -> catalog_book, status, target_date, notes, created_at
                                 (one user cannot add the same book twice)
"""
from django.conf import settings
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

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class ReadingListItem(models.Model):
    """A book that ONE user wants to read. Every user has a private reading list."""

    class Status(models.TextChoices):
        WANT_TO_READ = "WANT_TO_READ", "Want to read"
        READING = "READING", "Reading"
        FINISHED = "FINISHED", "Finished"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reading_list")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reading_list_items")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.WANT_TO_READ)
    target_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        constraints = [
            models.UniqueConstraint(fields=["user", "book"], name="unique_book_per_user"),
        ]

    def __str__(self):
        return f"{self.user} -> {self.book} ({self.get_status_display()})"
