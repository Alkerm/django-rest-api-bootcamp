from rest_framework.routers import DefaultRouter

from .views import BookViewSet, ReadingListItemViewSet

router = DefaultRouter()
router.register("books", BookViewSet, basename="book")
router.register("reading-list", ReadingListItemViewSet, basename="readinglistitem")

urlpatterns = router.urls
