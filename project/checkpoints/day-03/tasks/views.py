"""
Task API - one function view per CRUD operation.

    list_tasks    GET          /api/tasks/
    create_task   POST         /api/tasks/create/
    get_task      GET          /api/tasks/<pk>/
    update_task   PUT / PATCH  /api/tasks/<pk>/update/
    delete_task   DELETE       /api/tasks/<pk>/delete/

Day 3: TaskSerializer converts tasks to JSON and validates every input (yesterday's task_to_dict is gone).
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@api_view(["GET"])
def list_tasks(request):
    # TODO [Day 3 · P2a]: Return every task through TaskSerializer (many=True).
    # HINT: days/day-03/hints.md#p2  |  Example: days/day-03/example/views.py
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["POST"])
def create_task(request):
    # TODO [Day 3 · P3]: Validate request.data with TaskSerializer.
    #   invalid -> 400 with serializer.errors (nothing saved)
    #   valid   -> save with owner = the logged-in user, then 201 with serializer.data
    # HINT: days/day-03/hints.md#p3  |  Example: days/day-03/example/views.py (create_movie)
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["GET"])
def get_task(request, pk):
    # TODO [Day 3 · P2b]: Return one task through TaskSerializer (unknown id -> 404).
    # HINT: days/day-03/hints.md#p2
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["PUT", "PATCH"])
def update_task(request, pk):
    # TODO [Day 3 · P4]: Update through TaskSerializer: partial for PATCH, every required field for PUT.
    #   invalid -> 400 with serializer.errors;  valid -> save, 200 with serializer.data
    # HINT: days/day-03/hints.md#p4
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["DELETE"])
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
