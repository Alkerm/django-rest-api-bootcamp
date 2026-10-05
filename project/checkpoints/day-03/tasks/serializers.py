from django.utils import timezone
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Translator + gatekeeper: Task <-> JSON, and rejects invalid input before saving."""

    # TODO [Day 3 · P6 - Day 2 review]: Show the owner's USERNAME instead of the numeric user id.
    #   Declare `owner` as a read-only field whose source is "owner.username".
    #   Expected in responses:  "owner": "alice"   (instead of "owner": 1)
    # HINT: days/day-03/hints.md#p6  |  Example: days/day-02/example/serializers.py
    # YOUR CODE HERE

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "due_date",
            "owner",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "owner", "created_at", "updated_at"]
        # DRF already rejects a missing/blank title and an unknown status value (status has choices).
        # TODO [Day 3 · P7]: Make the title errors clear for API clients with extra_kwargs:
        #   missing title  -> "Title is required."
        #   blank title    -> "Title cannot be blank."   ("   " counts as blank - DRF trims whitespace)
        # HINT: days/day-03/hints.md#p7
        # YOUR CODE HERE

    # TODO [Day 3 · P8]: Reject a due_date earlier than today - but only when CREATING a task.
    #   - Field-level validator name: validate_<field_name>
    #   - On create, self.instance is None (on update it is the existing Task).
    #   - Use timezone.localdate() for "today" (Riyadh time, see TIME_ZONE in settings).
    #   - due_date is optional: None must stay valid.
    #   Error message: "Due date cannot be earlier than today."
    # HINT: days/day-03/hints.md#p8  |  Example: days/day-03/example/serializers.py
    # YOUR CODE HERE
