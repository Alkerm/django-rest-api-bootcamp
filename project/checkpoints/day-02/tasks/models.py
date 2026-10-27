from django.conf import settings
from django.db import models


class Task(models.Model):
    """One to-do item that belongs to exactly one user (its owner)."""

    class Status(models.TextChoices):
        TODO = "TODO", "To do"
        IN_PROGRESS = "IN_PROGRESS", "In progress"
        DONE = "DONE", "Done"

    # `id` is created automatically by Django (BigAutoField) - do not add it yourself.

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    due_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO [Day 2 · P1 - Day 1 review]: Make the newest tasks come first in every list.
    #   Add an inner `class Meta` with ordering by created_at, newest first ("-created_at").
    #   Then run:  python manage.py makemigrations  and  python manage.py migrate
    # HINT: days/day-02/hints.md#p1  |  Example: days/day-01/example/models.py
    # YOUR CODE HERE

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
