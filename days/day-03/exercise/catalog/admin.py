from django.contrib import admin

from .models import Author, Book, ReadingListItem


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "country"]
    search_fields = ["name"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "published_year", "available_copies"]
    list_filter = ["author"]
    search_fields = ["title", "isbn"]


@admin.register(ReadingListItem)
class ReadingListItemAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "book", "status", "target_date", "created_at"]
    list_filter = ["user", "status"]
