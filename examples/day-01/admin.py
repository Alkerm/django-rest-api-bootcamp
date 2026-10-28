"""Day 1 worked example - registering models in the Django admin."""
from django.contrib import admin

from .models import Director, Movie

# Simplest form: default list page (shows __str__ only)
admin.site.register(Director)


# Customised form: a ModelAdmin class + the @admin.register decorator
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "genre", "release_date", "director"]   # table columns
    list_filter = ["genre", "director"]                                    # filter sidebar
    search_fields = ["title", "imdb_code"]                                 # search box
