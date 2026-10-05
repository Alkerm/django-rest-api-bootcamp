"""
URL configuration for the Task Management API.

/admin/      Django admin
/api/        Task API (Day 2)
/api-auth/   Browsable-API login/logout - a temporary development bridge until token auth on Day 3
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # TODO [Day 2 · P6]: Connect the tasks app's routes under "api/"
    #   and DRF's login/logout views under "api-auth/".
    # HINT: days/day-02/hints.md#p6
    # YOUR CODE HERE
]
