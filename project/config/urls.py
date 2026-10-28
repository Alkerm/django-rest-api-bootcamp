"""
URL configuration for the Task Management API.

/admin/      Django admin
/api/        Task API (tasks/urls.py)
/api-auth/   Browsable-API login/logout: log in here to use the API in the browser
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # TODO [P10]: Connect the tasks app's routes under "api/"
    #   and DRF's login/logout views under "api-auth/".
    # HINT: HINTS.md#p10
    # YOUR CODE HERE
]
