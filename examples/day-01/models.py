"""
Day 1 worked example - a small MOVIES app (a different domain from the exercise and the project).

Read it next to your TODOs: the same Django building blocks, different names.
"""
from django.conf import settings
from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=120)          # short text, max length required
    birth_year = models.PositiveIntegerField(null=True, blank=True)  # optional number

    def __str__(self):
        return self.name


class Movie(models.Model):
    # 1) CHOICES - a fixed list of allowed values: (stored value, human label)
    class Genre(models.TextChoices):
        DRAMA = "DRAMA", "Drama"
        COMEDY = "COMEDY", "Comedy"
        DOCUMENTARY = "DOCUMENTARY", "Documentary"

    # 2) FIELDS
    title = models.CharField(max_length=200)                      # required text
    summary = models.TextField(blank=True)                         # long text, may be empty in forms
    genre = models.CharField(                                      # text limited to the choices
        max_length=20,
        choices=Genre.choices,
        default=Genre.DRAMA,
    )
    release_date = models.DateField(null=True, blank=True)        # optional date (NULL in the database)
    imdb_code = models.CharField(max_length=12, unique=True)       # no two rows may share this value

    # 3) RELATIONSHIPS - ForeignKey = "many movies belong to one director"
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,     # deleting the director deletes their movies
        related_name="movies",        # director.movies.all()
    )
    # A ForeignKey to Django's built-in user model (use settings.AUTH_USER_MODEL, not User directly):
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="movies")

    # 4) AUTOMATIC TIMESTAMPS
    created_at = models.DateTimeField(auto_now_add=True)   # set ONCE when the row is created
    updated_at = models.DateTimeField(auto_now=True)       # set on EVERY save()

    # 5) META - model-wide options
    class Meta:
        ordering = ["-release_date"]   # "-" = descending (newest first)

    # 6) __str__ - how the object is shown in the admin and the shell
    def __str__(self):
        # get_<field>_display() returns the human label of a choice field: "Drama"
        return f"{self.title} ({self.get_genre_display()})"
