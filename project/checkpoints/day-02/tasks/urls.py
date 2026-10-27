from django.urls import path

from . import views

urlpatterns = [
    # TODO [Day 2 · P7]: One path() per view, mounted under /api/ by config/urls.py:
    #   tasks/                    list_tasks    name="task-list"
    #   tasks/create/             create_task   name="task-create"
    #   tasks/<int:pk>/           get_task      name="task-detail"
    #   tasks/<int:pk>/update/    update_task   name="task-update"
    #   tasks/<int:pk>/delete/    delete_task   name="task-delete"
    # HINT: days/day-02/hints.md#p7  |  Example: days/day-02/example/urls.py
    # YOUR CODE HERE
]
