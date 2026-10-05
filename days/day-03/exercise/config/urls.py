from django.contrib import admin
from django.urls import include, path
# TODO [Day 3 · Task 1c - part 1]: Import obtain_auth_token from rest_framework.authtoken.views
#   (only AFTER "rest_framework.authtoken" is in INSTALLED_APPS - otherwise Django refuses to start).
# HINT: days/day-03/hints.md#task-1
# YOUR CODE HERE

urlpatterns = [
    path("admin/", admin.site.urls),
    # TODO [Day 3 · Task 1c - part 2]: Add the token login endpoint "api/auth/token/" using obtain_auth_token.
    #   POST {"username": "alice", "password": "..."}  ->  200 {"token": "<40 characters>"}
    # HINT: days/day-03/hints.md#task-1
    # YOUR CODE HERE
    path("api/", include("catalog.urls")),
    path("api-auth/", include("rest_framework.urls")),  # browsable-API login (optional)
]
