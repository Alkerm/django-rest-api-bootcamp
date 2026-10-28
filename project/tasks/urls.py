from django.urls import path

from . import views

urlpatterns = [
    # TODO [P9]: One path() per view, mounted under /api/ by config/urls.py:
    #   tasks/                    list_tasks    name="task-list"
    #   tasks/create/             create_task   name="task-create"
    #   tasks/<int:pk>/           get_task      name="task-detail"
    #   tasks/<int:pk>/update/    update_task   name="task-update"
    #   tasks/<int:pk>/delete/    delete_task   name="task-delete"
    # HINT: HINTS.md#p9  |  Example: examples/day-02/urls.py
    # YOUR CODE HERE
]
