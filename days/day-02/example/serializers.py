"""
Day 2 worked example - serializers for the Movies domain (see day-01/example/models.py for the models).

A serializer is a TRANSLATOR (model <-> JSON) and a GATEKEEPER (rejects invalid input before saving).
"""
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


# What the serializer does, step by step (try it in `python manage.py shell`):
#
#   movie = Movie.objects.first()
#   MovieSerializer(movie).data                 -> {"id": 1, "title": "Inception", ...}   (model -> Python dict -> JSON)
#
#   s = MovieSerializer(data={"title": "", "director": 999})
#   s.is_valid()                                -> False
#   s.errors                                    -> {"title": ["This field may not be blank."],
#                                                   "director": ['Invalid pk "999" - object does not exist.'], ...}
#
#   s = MovieSerializer(data={"title": "Dune", "imdb_code": "tt1160419", "director": 1})
#   s.is_valid()                                -> True
#   s.save(added_by=request.user)               -> creates the row; extra keyword arguments are saved too
