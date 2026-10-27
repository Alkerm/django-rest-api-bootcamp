"""
Task API - one function view per CRUD operation.

    list_tasks    GET          /api/tasks/
    create_task   POST         /api/tasks/create/
    get_task      GET          /api/tasks/<pk>/
    update_task   PUT / PATCH  /api/tasks/<pk>/update/
    delete_task   DELETE       /api/tasks/<pk>/delete/

Security layers (Day 4):
    1. IsAuthenticated (settings)      -> anonymous callers get 401 before a view runs
    2. every query filters by owner    -> a user only ever "sees" their own tasks (others' tasks -> 404)
    3. owner is read-only, set on save -> the owner always comes from the token, never from the request body
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


def get_own_task(request, pk):
    """Find one task by id - but only among the caller's own tasks. Used by get, update and delete."""
    # TODO [Day 4 · P5]: Look the task up by pk AND owner=request.user.
    #   Another user's task must answer 404, exactly like an id that does not exist.
    # HINT: days/day-04/hints.md#p5  |  Example: days/day-04/example/views.py (get_own_note)
    # YOUR CODE HERE - replace the placeholder line below
    return get_object_or_404(Task, pk=pk)


@api_view(["GET"])
def list_tasks(request):
    # TODO [Day 4 · P4]: Replace "all tasks" with "only my tasks" (owner = request.user).
    # HINT: days/day-04/hints.md#p4  |  Example: days/day-04/example/views.py (list_notes)
    # YOUR CODE HERE - replace the placeholder line below
    tasks = Task.objects.all()
    return Response(TaskSerializer(tasks, many=True).data)


@api_view(["POST"])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save(owner=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_task(request, pk):
    task = get_own_task(request, pk)
    return Response(TaskSerializer(task).data)


@api_view(["PUT", "PATCH"])
def update_task(request, pk):
    task = get_own_task(request, pk)
    serializer = TaskSerializer(task, data=request.data, partial=request.method == "PATCH")
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_task(request, pk):
    task = get_own_task(request, pk)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
