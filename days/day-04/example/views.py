"""
Day 4 worked example - a PERSONAL NOTES API where every user only sees their own notes.

Model (notes/models.py):
    class Note(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notes")
        text = models.TextField()
        remind_on = models.DateField(null=True, blank=True)

URLs (notes/urls.py) - the same path() style as Days 2-3:
    notes/                    list_notes     notes/<int:pk>/          get_note
    notes/create/             create_note    notes/<int:pk>/update/   update_note
                                             notes/<int:pk>/delete/   delete_note

Security layers:
    1. IsAuthenticated (DEFAULT_PERMISSION_CLASSES in settings) -> no / bad token = 401, the view never runs
    2. every query is filtered by request.user                  -> another user's note = 404
    3. author is read-only and set with save(author=...)        -> a client can never choose the author
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer


def get_own_note(request, pk):
    # INSECURE (Day 2-3 style):  get_object_or_404(Note, pk=pk)   -> anyone can read anyone's note by guessing ids
    # SECURE: the lookup itself contains the owner. Someone else's note does not exist FOR YOU -> 404.
    return get_object_or_404(Note, pk=pk, author=request.user)


@api_view(["GET"])
@permission_classes([IsAuthenticated])   # optional here: the same rule is already the default in settings
def list_notes(request):
    # INSECURE:  Note.objects.all()  -> every user sees every note
    notes = Note.objects.filter(author=request.user)
    return Response(NoteSerializer(notes, many=True).data)


@api_view(["POST"])
def create_note(request):
    serializer = NoteSerializer(data=request.data, context={"request": request})
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save(author=request.user)          # the author comes from the TOKEN, never from the body
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_note(request, pk):
    return Response(NoteSerializer(get_own_note(request, pk)).data)


@api_view(["PUT", "PATCH"])
def update_note(request, pk):
    note = get_own_note(request, pk)
    serializer = NoteSerializer(note, data=request.data, partial=request.method == "PATCH",
                                context={"request": request})
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_note(request, pk):
    get_own_note(request, pk).delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
