"""
Day 3 worked example - Day 2's function views, rewritten with MovieSerializer.

The URLs do not change at all (see days/day-02/example/urls.py). Compare each view with its Day 2 version:
every movie_to_dict() and every hand-written input check is gone.
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer


@api_view(["GET"])
def list_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)     # many=True: a queryset in -> a list of dicts out
    return Response(serializer.data)


@api_view(["POST"])
def create_movie(request):
    serializer = MovieSerializer(data=request.data)      # data= : INPUT to validate
    if not serializer.is_valid():                        # runs ALL rules: built-in, validate_<field>, validate
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   # {"field": ["message"]}
    serializer.save(added_by=request.user)               # INSERT; extra keyword arguments = server-side values
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return Response(MovieSerializer(movie).data)        # an object in -> one dict out


@api_view(["PUT", "PATCH"])
def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    # instance + data = UPDATE. partial=True (PATCH): only the sent fields are validated and changed.
    # partial=False (PUT): every required field must be sent, otherwise 400.
    serializer = MovieSerializer(movie, data=request.data, partial=request.method == "PATCH")
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()                                    # UPDATE ... WHERE id = pk
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)              # unchanged: no JSON in, no JSON out
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
