"""
Day 3 worked example - an object-level permission.

has_permission(request, view)              -> checked for EVERY request (e.g. "is the user logged in?")
has_object_permission(request, view, obj)  -> checked when ONE object is accessed (retrieve/update/delete)
Return True to allow, False to deny (DRF then answers 403 with `message`).
"""
from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    message = "You can only access your own notes."

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Variation: anyone may READ (GET, HEAD, OPTIONS), only the author may change."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
