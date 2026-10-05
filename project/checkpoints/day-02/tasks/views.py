from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    One class -> six operations:
        list (GET /api/tasks/)          create (POST /api/tasks/)
        retrieve (GET /api/tasks/{id}/) update (PUT) / partial_update (PATCH) / destroy (DELETE)
    """

    # TODO [Day 2 · P3]: Tell the viewset WHICH rows it works on and HOW to convert them.
    #   queryset         -> all Task objects (Day 3 will restrict this to the current user)
    #   serializer_class -> the serializer you wrote in serializers.py
    # HINT: days/day-02/hints.md#p3  |  Example: days/day-02/example/views.py
    # YOUR CODE HERE

    # TODO [Day 2 · P4]: The client never chooses the owner - the server does.
    #   Override perform_create() so the new task is saved with owner = the logged-in user.
    # HINT: days/day-02/hints.md#p4
    # YOUR CODE HERE
