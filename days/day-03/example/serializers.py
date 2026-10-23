"""
Day 3 worked example - a serializer for the Movies domain (see day-01/example/models.py for the models).

A serializer is a TRANSLATOR (model <-> JSON) and a GATEKEEPER (rejects invalid input before saving).
It replaces Day 2's hand-written movie_to_dict() and the if-statements that checked the input.

Three levels of validation:
  1. Built-in    : from the model fields (required, max_length, choices, unique, ForeignKey exists ...) - no code
  2. Field-level : def validate_<field>(self, value)  -> one field; the error appears under that field's name
  3. Object-level: def validate(self, attrs)          -> rules that combine several fields ("non_field_errors")
Raise serializers.ValidationError("message") to reject; return the value (or attrs) to accept.
"""
from django.utils import timezone
from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # Extra READ-ONLY field taken from a related object: movie.director.name
    director_name = serializers.ReadOnlyField(source="director.name")

    # Show the user who added the movie by username instead of id (source can follow relationships)
    added_by = serializers.ReadOnlyField(source="added_by.username")

    class Meta:
        model = Movie
        # Which fields appear in the JSON, in this order
        fields = [
            "id",
            "title",
            "genre",
            "release_date",
            "director",        # writable: the client sends the director's id, e.g. 3
            "director_name",   # read-only (declared above)
            "added_by",        # read-only (declared above)
            "created_at",
        ]
        # Fields the client may SEE but never SET (the server controls them)
        read_only_fields = ["id", "created_at"]
        # VALIDATION 1 - custom texts for DRF's built-in errors (required / blank / max_length ...)
        extra_kwargs = {
            "title": {"error_messages": {"required": "A movie needs a title.", "blank": "Title cannot be blank."}},
        }

    # VALIDATION 2 - a field-level rule: DRF calls validate_<field_name>(value) automatically.
    #   Raise serializers.ValidationError("message") to reject  -> 400 {"release_date": ["message"]}
    #   Return the value to accept it.
    def validate_release_date(self, value):
        # self.instance is None when CREATING, and the existing Movie when UPDATING (PUT/PATCH).
        # Here the rule applies to creates only, so an old movie can still be edited.
        if self.instance is None and value is not None and value > timezone.localdate():
            raise serializers.ValidationError("Release date cannot be in the future.")
        return value

    # VALIDATION 3 - an object-level rule: DRF calls validate(attrs) after every field passed on its own.
    #   attrs is a dict of the validated fields. On PATCH a field may be missing -> fall back to self.instance.
    def validate(self, attrs):
        genre = attrs.get("genre", self.instance.genre if self.instance else Movie.Genre.DRAMA)
        release_date = attrs.get("release_date", self.instance.release_date if self.instance else None)
        if genre == Movie.Genre.DOCUMENTARY and release_date is None:
            raise serializers.ValidationError("A documentary needs a release date.")
        return attrs


# What the serializer does, step by step (try it in `python manage.py shell`):
#
#   movie = Movie.objects.first()
#   MovieSerializer(movie).data                 -> {"id": 1, "title": "Inception", ...}   (model -> Python dict -> JSON)
#
#   s = MovieSerializer(data={"title": "", "director": 999})
#   s.is_valid()                                -> False
#   s.errors                                    -> {"title": ["Title cannot be blank."],
#                                                   "director": ['Invalid pk "999" - object does not exist.'], ...}
#
#   s = MovieSerializer(data={"title": "Dune", "imdb_code": "tt1160419", "director": 1})
#   s.is_valid()                                -> True
#   s.save(added_by=request.user)               -> creates the row; extra keyword arguments are saved too
