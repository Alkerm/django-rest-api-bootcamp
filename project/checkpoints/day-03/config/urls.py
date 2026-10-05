"""
URL configuration for the Task Management API.

/admin/             Django admin
/api/auth/token/    Exchange username + password for an API token (Day 3)
/api/               Task API
/api-auth/          Browsable-API login/logout (handy while developing)
"""
from django.contrib import admin
from django.urls import include, path
# TODO [Day 3 · P3 - part 1]: Import obtain_auth_token from rest_framework.authtoken.views
#   (only AFTER "rest_framework.authtoken" is in INSTALLED_APPS - otherwise Django refuses to start).
# HINT: days/day-03/hints.md#p3
# YOUR CODE HERE

urlpatterns = [
    path("admin/", admin.site.urls),
    # TODO [Day 3 · P3 - part 2]: Add the token login endpoint at "api/auth/token/" using obtain_auth_token.
    #   Give it name="api-token".
    #   POST {"username": "...", "password": "..."}  ->  200 {"token": "..."}
    # HINT: days/day-03/hints.md#p3
    # YOUR CODE HERE
    path("api/", include("tasks.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
