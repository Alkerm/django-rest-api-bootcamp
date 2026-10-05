"""
Day 4 worked example - reading configuration from environment variables.

Environment variables are always TEXT (or missing). os.getenv(name, default) returns the text, or the default.
Convert the text to the Python type you need.
"""
import os

# A plain string with a safe development default
API_TITLE = os.getenv("API_TITLE", "Notes API (development)")

# A boolean: compare the lower-cased text.  "True", "true", "TRUE" -> True ; "False", "0", "" -> False
MAINTENANCE_MODE = os.getenv("MAINTENANCE_MODE", "False").lower() == "true"
# WRONG: bool(os.getenv("MAINTENANCE_MODE"))  -> bool("False") is True, because any non-empty text is True!

# An integer
PAGE_SIZE = int(os.getenv("PAGE_SIZE", "20"))

# A list from comma-separated text: "a.com, b.com," -> ["a.com", "b.com"]
TRUSTED_SITES = [site.strip() for site in os.getenv("TRUSTED_SITES", "localhost").split(",") if site.strip()]


# Setting variables for ONE terminal session:
#   Windows PowerShell:   $env:PAGE_SIZE = "50"        remove: Remove-Item Env:PAGE_SIZE
#   macOS / Linux:        export PAGE_SIZE=50          remove: unset PAGE_SIZE
#   one command only (macOS / Linux):   PAGE_SIZE=50 python manage.py runserver
#
# .env.example documents every variable with PLACEHOLDER values and IS committed.
# Real values (.env, Render dashboard) are NEVER committed.
