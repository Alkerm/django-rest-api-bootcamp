"""
Day 3 worked example - validation in a serializer (Notes domain).

Three levels of validation:
  1. Built-in   : from the model/field (required, max_length, choices, unique ...) - no code needed
  2. Field-level: def validate_<field>(self, value)   -> one field, error appears under that field name
  3. Object-level: def validate(self, attrs)          -> rules that combine several fields
Raise serializers.ValidationError("message") to reject; return the (possibly cleaned) value to accept.
The view then answers 400 with {"field": ["message"]}.
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
