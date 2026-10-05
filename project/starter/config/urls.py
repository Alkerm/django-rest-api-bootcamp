"""
URL configuration for the Task Management API.

Day 1: only the admin site. API routes are added on Day 2.
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
