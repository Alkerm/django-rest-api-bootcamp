"""
URL configuration for the Task Management API.

/admin/             Django admin
/api/auth/token/    Exchange username + password for an API token (Day 3)
/api/               Task API
/api-auth/          Browsable-API login/logout (handy while developing)
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/token/", obtain_auth_token, name="api-token"),
    path("api/", include("tasks.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
