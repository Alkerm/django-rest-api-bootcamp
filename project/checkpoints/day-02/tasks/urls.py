from rest_framework.routers import DefaultRouter

from .views import TaskViewSet

router = DefaultRouter()

# TODO [Day 2 · P5]: Register TaskViewSet on the router under the prefix "tasks".
#   Use basename="task" -> the router then names the routes "task-list" and "task-detail".
#   Result: /api/tasks/ (list + create) and /api/tasks/{id}/ (retrieve, update, delete).
# HINT: days/day-02/hints.md#p5  |  Example: days/day-02/example/urls.py
# YOUR CODE HERE

urlpatterns = router.urls
