from django.utils import timezone
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Translator + gatekeeper: Task <-> JSON, and rejects invalid input before saving."""

    owner = serializers.ReadOnlyField(source="owner.username")

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
