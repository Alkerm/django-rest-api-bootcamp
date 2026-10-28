"""
Task API - one function view per CRUD operation.

    list_tasks    GET          /api/tasks/
    create_task   POST         /api/tasks/create/
    get_task      GET          /api/tasks/<pk>/
    update_task   PUT / PATCH  /api/tasks/<pk>/update/
    delete_task   DELETE       /api/tasks/<pk>/delete/

Every view follows the same pattern:
    1. @api_view([...])  -> which HTTP methods this URL accepts (others get 405)
    2. ORM               -> read or change rows
    3. TaskSerializer    -> object -> JSON (output) and JSON -> validated data (input)
    4. Response(...)     -> the data + a status code
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@api_view(["GET"])
def list_tasks(request):
    # TODO [P5a]: Return every task as JSON: TaskSerializer(..., many=True).data  (200).
    # HINT: HINTS.md#p5  |  Example: examples/day-03/views.py (list_movies)
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["GET"])
def get_task(request, pk):
    # TODO [P5b]: Return one task through TaskSerializer (200); an unknown id -> 404.
    # HINT: HINTS.md#p5  |  Example: examples/day-03/views.py (get_movie)
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["POST"])
def create_task(request):
    # TODO [P6]: Validate request.data with TaskSerializer.
    #   invalid -> 400 with serializer.errors (nothing saved)
    #   valid   -> save with owner = the logged-in user (request.user), then 201 with serializer.data
    # HINT: HINTS.md#p6  |  Example: examples/day-03/views.py (create_movie)
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["PUT", "PATCH"])
def update_task(request, pk):
    # TODO [P7]: Update the task through TaskSerializer (unknown id -> 404).
    #   partial=True for PATCH (only some fields), partial=False for PUT (every required field).
    #   invalid -> 400 with serializer.errors;  valid -> save, 200 with serializer.data
    # HINT: HINTS.md#p7  |  Example: examples/day-03/views.py (update_movie)
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["DELETE"])
def delete_task(request, pk):
    # TODO [P8]: Delete the task and return 204 with an empty body; an unknown id -> 404.
    # HINT: HINTS.md#p8  |  Example: examples/day-02/views.py (delete_movie)
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
