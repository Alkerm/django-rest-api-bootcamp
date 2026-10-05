"""Day 2 worked example - viewsets for the Movies domain."""
from rest_framework import viewsets

from .models import Director, Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet = list + create + retrieve + update + partial_update + destroy.
    Two attributes are enough:
        queryset          WHICH rows this endpoint works with
        serializer_class  HOW to convert / validate them
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # Hook called by `create` after validation succeeds - the place for server-side values.
    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class DirectorViewSet(viewsets.ReadOnlyModelViewSet):
    """ReadOnlyModelViewSet = only list + retrieve (GET). POST/PUT/PATCH/DELETE return 405."""

    queryset = Director.objects.all()
    # serializer_class = DirectorSerializer   (written like MovieSerializer)


# Other base classes you may meet:
#   viewsets.GenericViewSet  - no actions at all, you add mixins yourself
#   generics.ListCreateAPIView / RetrieveUpdateDestroyAPIView - the same logic as two separate views (no router)
