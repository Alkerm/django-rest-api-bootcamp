"""
Task API - one function view per CRUD operation.

    list_tasks    GET          /api/tasks/
    create_task   POST         /api/tasks/create/
    get_task      GET          /api/tasks/<pk>/
    update_task   PUT / PATCH  /api/tasks/<pk>/update/
    delete_task   DELETE       /api/tasks/<pk>/delete/

Day 2: objects are converted to dicts by hand. Day 3 replaces that with a serializer.
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task


def task_to_dict(task):
    # TODO [Day 2 · P2]: Return a dict with the 8 fields of the API, in this order:
    #   id, title, description, status, due_date, owner, created_at, updated_at
    #   "owner" is the owner's id (task.owner_id).
    # HINT: days/day-02/hints.md#p2  |  Example: days/day-02/example/views.py (movie_to_dict)
    # YOUR CODE HERE - replace the placeholder line below
    return {"id": task.id}


@api_view(["GET"])
def list_tasks(request):
    # TODO [Day 2 · P3a]: Return every task as a list of dicts (200).
    # HINT: days/day-02/hints.md#p3
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["POST"])
def create_task(request):
    # TODO [Day 2 · P3b]: Create a task from request.data and return it with status 201.
    #   - A missing or blank title -> 400 {"title": ["Title is required."]} and nothing is saved.
    #   - description, status and due_date are optional (defaults: "", "TODO", None).
    #   - The owner is the logged-in user (request.user), NEVER a value from the request body.
    # HINT: days/day-02/hints.md#p3  |  Example: days/day-02/example/views.py (create_movie)
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["GET"])
def get_task(request, pk):
    # TODO [Day 2 · P4]: Return one task (200); an unknown id -> 404.
    # HINT: days/day-02/hints.md#p4
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


UPDATABLE_FIELDS = ["title", "description", "status", "due_date"]   # owner, id and timestamps are never updated


@api_view(["PUT", "PATCH"])
def update_task(request, pk):
    # TODO [Day 2 · P5]: Change only the fields in UPDATABLE_FIELDS that were sent, save, return 200.
    #   An unknown id -> 404.
    # HINT: days/day-02/hints.md#p5
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(["DELETE"])
def delete_task(request, pk):
    # TODO [Day 2 · P6]: Delete the task and return 204 with an empty body; an unknown id -> 404.
    # HINT: days/day-02/hints.md#p6
    # YOUR CODE HERE - replace the placeholder line below
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
