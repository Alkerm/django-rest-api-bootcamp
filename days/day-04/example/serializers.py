"""
Day 4 worked example - the NoteSerializer used by views.py (serializers and validation are Day 3 material).

Two details matter for security:
  - author is READ-ONLY: the client can never choose or change it; the view passes it to save().
  - validate_text() needs the current user: the view passes it in context={"request": request}.
"""
from django.utils import timezone
from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Note
        fields = ["id", "author", "text", "remind_on"]
        # Custom texts for built-in errors:
        extra_kwargs = {
            "text": {"error_messages": {"blank": "A note needs some text.", "required": "Text is required."}},
        }

    # 2) FIELD-LEVEL: the reminder date cannot be in the past.
    def validate_remind_on(self, value):
        # self.instance is None when CREATING, and the existing Note when UPDATING.
        is_create = self.instance is None
        if is_create and value is not None and value < timezone.localdate():
            raise serializers.ValidationError("Reminder date cannot be in the past.")
        return value

    # Field-level rule that needs the current user: the request is in self.context.
    def validate_text(self, value):
        user = self.context["request"].user
        same_text = Note.objects.filter(author=user, text=value)
        if self.instance is not None:
            same_text = same_text.exclude(pk=self.instance.pk)  # editing a note must not clash with itself
        if same_text.exists():
            raise serializers.ValidationError("You already have a note with this text.")
        return value

    # 3) OBJECT-LEVEL: rules across fields (attrs holds every validated field).
    def validate(self, attrs):
        if attrs.get("remind_on") and len(attrs.get("text", "")) < 3:
            raise serializers.ValidationError("A reminder needs a text of at least 3 characters.")
        return attrs
