"""
Day 2 worked example - plain path() routing: one URL per function view.

    path(<url pattern>, <view function>, name=<url name>)

    URL                         name            method   view
    movies/                     movie-list      GET      list_movies
    movies/create/              movie-create    POST     create_movie
    movies/<int:pk>/            movie-detail    GET      get_movie
    movies/<int:pk>/update/     movie-update    PUT      update_movie
                                                PATCH
    movies/<int:pk>/delete/     movie-delete    DELETE   delete_movie

<int:pk> is a path converter: it matches a whole number and passes it to the view as the argument `pk`.
/movies/7/ -> get_movie(request, pk=7).    /movies/abc/ -> no match -> 404.
The name lets you build a URL without typing it: reverse("movie-detail", args=[7]) -> "/api/movies/7/"
"""
from django.urls import path

from . import views

urlpatterns = [
    path("movies/", views.list_movies, name="movie-list"),
    path("movies/create/", views.create_movie, name="movie-create"),
    path("movies/<int:pk>/", views.get_movie, name="movie-detail"),
    path("movies/<int:pk>/update/", views.update_movie, name="movie-update"),
    path("movies/<int:pk>/delete/", views.delete_movie, name="movie-delete"),
]

# In the PROJECT's config/urls.py the app's routes are mounted under a prefix:
#
#   from django.urls import include, path
#   urlpatterns = [
#       path("api/", include("movies.urls")),             # -> /api/movies/, /api/movies/create/, ...
#       path("api-auth/", include("rest_framework.urls")), # login/logout links in the browsable API
#   ]
