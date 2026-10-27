"""
URL configuration for the Task Management API.

/admin/      Django admin
/api/        Task API (Day 2; serializer + validation on Day 3)
/api-auth/   Browsable-API login/logout - a temporary development bridge until token auth on Day 4
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tasks.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
