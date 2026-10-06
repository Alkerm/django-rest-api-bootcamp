from django.utils import timezone
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Translator + gatekeeper: Task <-> JSON, and rejects invalid input before saving."""

    # TODO [Day 3 · P6 · STRETCH (optional) - Day 2 review]: Show the owner's USERNAME instead of the numeric user id.
    #   Optional: without it the API is still correct, it just shows "owner": 1 instead of "owner": "alice".
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
        extra_kwargs = {
            "title": {
                "error_messages": {
                    "required": "Title is required.",
                    "blank": "Title cannot be blank.",
                }
            }
        }

    def validate_due_date(self, value):
        if self.instance is None and value is not None and value < timezone.localdate():
            raise serializers.ValidationError("Due date cannot be earlier than today.")
        return value
