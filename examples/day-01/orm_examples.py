"""
Day 1 worked example - the Django ORM cheat sheet (Movies domain).

Each line shows Python on the left and the SQL idea on the right.
Try these in `python manage.py shell` of any project that has similar models.
"""
from .models import Director, Movie

# ---------------------------------------------------------------- CREATE  (INSERT)
nolan = Director.objects.create(name="Christopher Nolan", birth_year=1970)
movie = Movie(title="Inception", imdb_code="tt1375666", director=nolan, added_by_id=1)
movie.save()                                       # INSERT happens on save()

# ---------------------------------------------------------------- READ  (SELECT)
Movie.objects.all()                                # SELECT * FROM movie
Movie.objects.count()                              # SELECT COUNT(*)
Movie.objects.get(id=1)                            # exactly ONE row (error if 0 or many)
Movie.objects.filter(genre="DRAMA")                # WHERE genre = 'DRAMA'
Movie.objects.exclude(genre="DRAMA")               # WHERE NOT genre = 'DRAMA'
Movie.objects.filter(release_date__year__gt=2010)  # __gt  greater than   (also __gte, __lt, __lte)
Movie.objects.filter(title__icontains="in")        # case-insensitive "contains"
Movie.objects.filter(director__name="Christopher Nolan")   # follow the ForeignKey with __
Movie.objects.order_by("title")                    # ORDER BY title       ("-title" = descending)
nolan.movies.all()                                 # reverse relationship via related_name
Movie.objects.values_list("title", flat=True)      # just the titles: <QuerySet ['Inception', ...]>
list(Movie.objects.values_list("title", flat=True))  # -> a plain Python list

# ---------------------------------------------------------------- UPDATE
movie.genre = Movie.Genre.DOCUMENTARY
movie.save()                                       # UPDATE ... WHERE id = movie.id
movie.refresh_from_db()                            # re-read the row to see what is really stored
Movie.objects.filter(genre="COMEDY").update(genre="DRAMA")   # bulk UPDATE, no save() needed

# ---------------------------------------------------------------- DELETE
movie.delete()                                     # DELETE ... WHERE id = movie.id
