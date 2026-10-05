from django.conf import settings
from django.db import models


class Task(models.Model):
    """One to-do item that belongs to exactly one user (its owner)."""

    class Status(models.TextChoices):
        # TODO [Day 1 · P2]: Define the three allowed status values.
        #   Stored value -> human label:  TODO -> "To do", IN_PROGRESS -> "In progress", DONE -> "Done"
        # HINT: days/day-01/hints.md#p2  |  Example: days/day-01/example/models.py
        # YOUR CODE HERE
        pass

    # `id` is created automatically by Django (BigAutoField) - do not add it yourself.

    # TODO [Day 1 · P3]: Add the remaining Task fields.
    #   field        type                                   rules
    #   title        CharField(max_length=200)              required
    #   description  TextField                              optional  -> blank=True
    #   status       CharField(max_length=20)               choices=Status.choices, default=Status.TODO
    #   due_date     DateField                              optional  -> null=True, blank=True
    #   owner        ForeignKey -> settings.AUTH_USER_MODEL  on_delete=CASCADE, related_name="tasks"
    #   created_at   DateTimeField                          set once on create -> auto_now_add=True
    #   updated_at   DateTimeField                          set on every save   -> auto_now=True
    # HINT: days/day-01/hints.md#p3  |  Example: days/day-01/example/models.py
    # YOUR CODE HERE

    def __str__(self):
        # TODO [Day 1 · P4]: Return a readable label, e.g. "Buy groceries (To do)".
        #   get_status_display() returns the human label of the status.
        # HINT: days/day-01/hints.md#p4
        # YOUR CODE HERE
        return super().__str__()
