"""
Day 1 exercise - Task 3B: talk to the database with the Django ORM.

BEFORE YOU START
    * Tasks 1 and 2 are done: the Book table exists and the sample data is loaded
      (python manage.py loaddata sample_data  ->  "Installed 9 object(s)").
    * Run this file from days/day-01/exercise with your .venv active:
          python orm_practice.py
    * The self-check at the bottom prints PASS/FAIL for every function.
      Core = functions 1-3 (3/5 passed). Functions 4-5 are STRETCH (optional): do them if you finish early.
      The check for function 5 creates a temporary book and deletes it again, so the sample data stays unchanged.

DATA YOU WORK WITH (pre-loaded sample data)
    catalog_author:  id | name                            | country
                     1  | Robert C. Martin                | United States
                     2  | Martin Fowler                   | United Kingdom
                     3  | Muhammad ibn Musa al-Khwarizmi  | Abbasid Caliphate (Baghdad)

    catalog_book:    id | title                                  | published_year | available_copies | author_id
                     1  | Clean Code                             | 2008           | 3                | 1
                     2  | The Clean Coder                        | 2011           | 0                | 1
                     3  | Clean Architecture                     | 2017           | 2                | 1
                     4  | Refactoring                            | 1999           | 4                | 2
                     5  | Patterns of Enterprise Application ... | 2002           | 1                | 2
                     6  | The Compendious Book on Calculation... | 820            | 0                | 3
"""
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from catalog.models import Author, Book  # noqa: E402  (must come after django.setup())


def count_books():
    """1. READ - How many books are in the library?   Expected: 6"""
    # TODO [Day 1 · Task 3B-1]: Return the number of Book rows.
    # HINT: days/day-01/hints.md#task-3
    # YOUR CODE HERE - replace the placeholder line below
    return None


def titles_by_author(author_name):
    """2. FILTER ACROSS A RELATIONSHIP - Titles of one author's books, sorted A-Z.
    Expected for "Martin Fowler": ["Patterns of Enterprise Application Architecture", "Refactoring"]"""
    # TODO [Day 1 · Task 3B-2]: Filter books by the author's NAME (double underscore: author__name),
    #   order by title, and return a plain list of titles.
    # YOUR CODE HERE - replace the placeholder line below
    return []


def count_published_after(year):
    """3. FIELD LOOKUP - How many books were published AFTER a year?   Expected for 2005: 3"""
    # TODO [Day 1 · Task 3B-3]: Use the __gt ("greater than") lookup on published_year.
    # YOUR CODE HERE - replace the placeholder line below
    return None


def available_titles():
    """4. FIELD LOOKUP - Titles of books that can be borrowed now (available_copies > 0), sorted A-Z.
    Expected: ["Clean Architecture", "Clean Code", "Patterns of Enterprise Application Architecture", "Refactoring"]"""
    # TODO [Day 1 · Task 3B-4 · STRETCH (optional)]
    # YOUR CODE HERE - replace the placeholder line below
    return []


def create_update_delete_book():
    """5. CREATE -> UPDATE -> DELETE one temporary book and report what happened.

    Steps (database change after each step):
        a. CREATE   Book(title="Temporary Book", isbn="9789999999999", published_year=2026,
                         available_copies=2, author=<Martin Fowler>)          -> 7 books in the table
        b. UPDATE   decrease available_copies by 1 and save()                   -> that row now has 1 copy
        c. DELETE   delete the book                                             -> 6 books again
    Return a tuple: (copies_after_update, books_after_delete)    Expected: (1, 6)
    """
    # TODO [Day 1 · Task 3B-5 · STRETCH (optional)]: Implement steps a, b and c.
    #   Get the author first: Author.objects.get(name="Martin Fowler")
    #   After save(), read the row again with refresh_from_db() to prove the DB really changed.
    # HINT: days/day-01/hints.md#task-3  |  Example: days/day-01/example/orm_examples.py
    # YOUR CODE HERE - replace the placeholder line below
    return (None, None)


# ---------------------------------------------------------------------- self-check (do not edit)
if __name__ == "__main__":
    NOT_STARTED = (None, [], (None, None))  # what the untouched placeholder lines return
    checks = [
        ("core", "1. count_books()", count_books, (), 6),
        ("core", "2. titles_by_author('Martin Fowler')", titles_by_author, ("Martin Fowler",),
         ["Patterns of Enterprise Application Architecture", "Refactoring"]),
        ("core", "3. count_published_after(2005)", count_published_after, (2005,), 3),
        ("stretch", "4. available_titles()", available_titles, (),
         ["Clean Architecture", "Clean Code", "Patterns of Enterprise Application Architecture", "Refactoring"]),
        ("stretch", "5. create_update_delete_book()", create_update_delete_book, (), (1, 6)),
    ]
    score = {"core": [0, 0], "stretch": [0, 0]}
    for level, label, function, args, expected in checks:
        score[level][1] += 1
        try:
            result = function(*args)
        except Exception as error:  # show the error but keep checking the rest
            result = f"ERROR: {type(error).__name__}: {error}"
        if result == expected:
            score[level][0] += 1
            print(f"[PASS] {label}")
        elif result in NOT_STARTED:
            print(f"[TODO] {label}  - not started yet" + ("  (stretch, optional)" if level == "stretch" else ""))
        else:
            print(f"[FAIL] {label}")
            print(f"        expected: {expected!r}")
            print(f"        got:      {result!r}")
    core, stretch = score["core"], score["stretch"]
    print()
    print(f"Core:    {core[0]}/{core[1]} passed")
    print(f"Stretch: {stretch[0]}/{stretch[1]} passed (optional)")
    if core[0] == core[1]:
        print()
        if stretch[0] < stretch[1]:
            print("Core done - well done! Move on to the project milestone, or try the stretch functions.")
        else:
            print("Everything passes - excellent work!")
