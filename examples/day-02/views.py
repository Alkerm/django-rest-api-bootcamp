"""
Day 2 worked example - function views for the Movies domain (see day-01/example/models.py for the models).

One function per CRUD operation. Each function:
    1. is decorated with @api_view([...]) -> DRF only lets the listed HTTP methods in (others get 405),
       parses the JSON body into request.data and renders the browsable API;
    2. talks to the database through the ORM (Day 1);
    3. returns Response(python_data, status=...) -> DRF turns the dict/list into JSON.

No serializer yet: we convert a Movie to a dict BY HAND (movie_to_dict) and read the input BY HAND.
On Day 3 a serializer replaces both jobs - you will see why it is worth it.
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Director, Movie


def movie_to_dict(movie):
    """Model object -> plain Python dict (JSON-ready). Choose the keys and their order yourself."""
    return {
        "id": movie.id,
        "title": movie.title,
        "genre": movie.genre,
        "release_date": movie.release_date,   # Response turns dates into "2010-07-16"
        "director": movie.director_id,        # the id of the related row
        "director_name": movie.director.name, # follow the relationship
        "created_at": movie.created_at,
    }


# ---------------------------------------------------------------- LIST    GET /api/movies/
@api_view(["GET"])
def list_movies(request):
    movies = Movie.objects.all()
    data = [movie_to_dict(movie) for movie in movies]
    return Response(data)                                   # 200 OK is the default status


# ---------------------------------------------------------------- CREATE  POST /api/movies/create/
@api_view(["POST"])
def create_movie(request):
    # request.data is the parsed JSON body: {"title": "Dune", "imdb_code": "tt1160419", "director": 1}
    title = request.data.get("title", "").strip()
    if not title:
        # Reject bad input BEFORE touching the database. Same shape DRF uses: {"field": ["message"]}
        return Response({"title": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

    director = get_object_or_404(Director, pk=request.data.get("director"))
    movie = Movie.objects.create(
        title=title,
        genre=request.data.get("genre", Movie.Genre.DRAMA),
        imdb_code=request.data.get("imdb_code", ""),
        director=director,
        added_by=request.user,           # the server decides who added it - never the client
    )
    return Response(movie_to_dict(movie), status=status.HTTP_201_CREATED)


# ---------------------------------------------------------------- RETRIEVE GET /api/movies/<pk>/
@api_view(["GET"])
def get_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)                 # unknown id -> 404 Not Found
    return Response(movie_to_dict(movie))


# ---------------------------------------------------------------- UPDATE  PUT/PATCH /api/movies/<pk>/update/
@api_view(["PUT", "PATCH"])
def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    # PATCH = change only the fields that were sent. (A strict PUT would require every field;
    # on Day 3 the serializer enforces that for you with partial=False.)
    if "title" in request.data:
        title = request.data["title"].strip()
        if not title:
            return Response({"title": ["This field may not be blank."]}, status=status.HTTP_400_BAD_REQUEST)
        movie.title = title
    if "genre" in request.data:
        movie.genre = request.data["genre"]

    movie.save()                                            # UPDATE ... WHERE id = pk
    return Response(movie_to_dict(movie))


# ---------------------------------------------------------------- DELETE  DELETE /api/movies/<pk>/delete/
@api_view(["DELETE"])
def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()                                          # DELETE FROM ... WHERE id = pk
    return Response(status=status.HTTP_204_NO_CONTENT)      # 204 = success, empty body


# Notice how much repeated, hand-written work there is:
#   - every field is copied into the dict by hand (and again when reading input);
#   - every rule ("title required", "director must exist", "genre must be a valid choice") is an if-statement;
#   - a wrong genre or a missing imdb_code is NOT caught here at all.
# Day 3: a SERIALIZER does all of this in a few declarative lines.
