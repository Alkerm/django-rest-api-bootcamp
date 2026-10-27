from django.urls import path

from . import views

urlpatterns = [
    path("tasks/", views.list_tasks, name="task-list"),
    path("tasks/create/", views.create_task, name="task-create"),
    path("tasks/<int:pk>/", views.get_task, name="task-detail"),
    path("tasks/<int:pk>/update/", views.update_task, name="task-update"),
    path("tasks/<int:pk>/delete/", views.delete_task, name="task-delete"),
]
