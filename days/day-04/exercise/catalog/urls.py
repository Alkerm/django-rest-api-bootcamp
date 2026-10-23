"""
Day 4 exercise - GIVEN: one path() per view (the same style as Days 2-3).
"""
from django.urls import path

from . import views

urlpatterns = [
    path("books/", views.list_books, name="book-list"),
    path("books/<int:pk>/", views.get_book, name="book-detail"),
    path("reading-list/", views.list_items, name="item-list"),
    path("reading-list/create/", views.create_item, name="item-create"),
    path("reading-list/<int:pk>/", views.get_item, name="item-detail"),
    path("reading-list/<int:pk>/update/", views.update_item, name="item-update"),
    path("reading-list/<int:pk>/delete/", views.delete_item, name="item-delete"),
]
