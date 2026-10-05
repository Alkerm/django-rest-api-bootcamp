"""
Day 3 worked example - a PERSONAL NOTES API where every user only sees their own notes.

Model (notes/models.py):
    class Note(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notes")
        text = models.TextField()
        remind_on = models.DateField(null=True, blank=True)
"""
from rest_framework import permissions, viewsets

from .models import Note
from .permissions import IsAuthor
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthor]

    # INSECURE (Day 2 style):  queryset = Note.objects.all()   -> every user sees every note
    #
    # SECURE: build the queryset per request, from the authenticated user.
    # list      -> only my notes
    # retrieve / update / delete of someone else's note -> 404 (it is not in "my" queryset)
    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

    # The author is NEVER taken from the request body - always from the token.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
