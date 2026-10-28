from django.utils import timezone
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Translator + gatekeeper: Task <-> JSON, and rejects invalid input before saving."""

    # TODO [P11 · STRETCH (optional)]: Show the owner's username instead of the numeric id.
    #   A read-only field with source="owner.username" (it stays read-only: the client never sets it).
    # HINT: HINTS.md#p11  |  Example: examples/day-03/serializers.py (added_by)
    # YOUR CODE HERE

    class Meta:
        model = Task
        # TODO [P2]: Choose the fields the API exposes and protect server-controlled ones.
        #   fields           -> these 8 fields, in this order:
        #                       id, title, description, status, due_date, owner, created_at, updated_at
        #   read_only_fields -> fields the client must NEVER set:
        #                       id, owner, created_at, updated_at
        # HINT: HINTS.md#p2  |  Example: examples/day-03/serializers.py
        # YOUR CODE HERE - replace the placeholder line below
        fields = ["id"]
        # DRF already rejects a missing/blank title and an unknown status value (status has choices).
        # TODO [P3]: Make the title errors clear for API clients with extra_kwargs:
        #   missing title  -> "Title is required."
        #   blank title    -> "Title cannot be blank."   ("   " counts as blank - DRF trims whitespace)
        # HINT: HINTS.md#p3  |  Example: examples/day-03/serializers.py
        # YOUR CODE HERE

    # TODO [P4]: Reject a due_date earlier than today - but only when CREATING a task.
    #   - Field-level validator name: validate_<field_name>
    #   - On create, self.instance is None (on update it is the existing Task).
    #   - Use timezone.localdate() for "today" (Riyadh time, see TIME_ZONE in settings).
    #   - due_date is optional: None must stay valid.
    #   Error message: "Due date cannot be earlier than today."
    # HINT: HINTS.md#p4  |  Example: examples/day-03/serializers.py (validate_release_date)
    # YOUR CODE HERE
