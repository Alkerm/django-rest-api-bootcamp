from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Translator + gatekeeper: Task <-> JSON, and rejects invalid input before saving."""

    class Meta:
        model = Task
        # TODO [Day 2 · P2]: Choose the fields the API exposes and protect server-controlled ones.
        #   fields           -> all 8 required fields:
        #                       id, title, description, status, due_date, owner, created_at, updated_at
        #   read_only_fields -> fields the client must NEVER set:
        #                       id, owner, created_at, updated_at
        # HINT: days/day-02/hints.md#p2  |  Example: days/day-02/example/serializers.py
        # YOUR CODE HERE - replace the placeholder line below
        fields = ["id"]
