from rest_framework import permissions, viewsets

from .models import Task
from .permissions import IsOwner
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    One class -> six operations:
        list (GET /api/tasks/)          create (POST /api/tasks/)
        retrieve (GET /api/tasks/{id}/) update (PUT) / partial_update (PATCH) / destroy (DELETE)

    Security layers (Day 3):
        1. IsAuthenticated  -> anonymous callers get 401
        2. get_queryset()   -> a user only ever "sees" their own tasks (others' tasks -> 404)
        3. IsOwner          -> object-level double check
        4. perform_create() -> the owner always comes from the token, never from the request body
    """

    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    # TODO [Day 3 · P4]: Replace "all tasks" with "only my tasks".
    #   Day 2 used:  queryset = Task.objects.all()   <- every user could see every task!
    #   Override get_queryset() and return only the tasks whose owner is self.request.user.
    # HINT: days/day-03/hints.md#p4  |  Example: days/day-03/example/views.py
    # YOUR CODE HERE
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
