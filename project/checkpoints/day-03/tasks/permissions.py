from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Object-level permission: only the owner of a task may see or change it.

    get_queryset() already hides other users' tasks (-> 404). This class is a second layer
    ("defense in depth") in case a future view forgets to filter its queryset.
    """

    message = "You can only access your own tasks."

    def has_object_permission(self, request, view, obj):
        # TODO [Day 3 · P5 · STRETCH (optional)]: Return True only when the task's owner is the user making the request.
        #   Optional because get_queryset() (P4) already hides other users' tasks; this is a second safety layer.
        # HINT: days/day-03/hints.md#p5  |  Example: days/day-03/example/permissions.py
        # YOUR CODE HERE - replace the placeholder line below
        return True
