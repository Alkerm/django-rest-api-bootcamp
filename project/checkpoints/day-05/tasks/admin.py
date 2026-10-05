from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "status", "due_date", "owner", "created_at"]
    list_filter = ["status", "owner"]
    search_fields = ["title"]
