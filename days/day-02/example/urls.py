"""
Day 2 worked example - routers generate the URLs of a viewset.

    router.register("movies", MovieViewSet, basename="movie")

produces:
    URL                 name            methods -> actions
    /movies/            movie-list      GET -> list,      POST -> create
    /movies/{pk}/       movie-detail    GET -> retrieve,  PUT -> update,  PATCH -> partial_update,  DELETE -> destroy

The router names are used in tests:  reverse("movie-list"), reverse("movie-detail", args=[3])
"""
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = router.urls

# In the PROJECT's config/urls.py the app's routes are mounted under a prefix:
#
#   from django.urls import include, path
#   urlpatterns = [
#       path("api/", include("movies.urls")),             # -> /api/movies/
#       path("api-auth/", include("rest_framework.urls")), # login/logout links in the browsable API
#   ]
