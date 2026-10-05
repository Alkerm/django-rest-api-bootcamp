"""
Day 2 exercise - Task 2: the router generates the URLs for each viewset.
"""
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register("authors", AuthorViewSet, basename="author")  # GIVEN

# TODO [Day 2 · Task 2b]: Register BookViewSet under the prefix "books" with basename="book".
# HINT: days/day-02/hints.md#task-2
# YOUR CODE HERE

urlpatterns = router.urls
