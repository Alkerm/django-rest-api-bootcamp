"""
Day 5 worked example - the production-related parts of settings.py, all driven by environment variables.

Same code runs on a laptop (no variables set -> safe development defaults) and on Render (variables set).
"""
import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "development-only-key")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",") if h.strip()]
CSRF_TRUSTED_ORIGINS = [o.strip() for o in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",") if o.strip()]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",       # directly after SecurityMiddleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    # ... the rest unchanged ...
]

# ---------------------------------------------------------------- database
# Default: local SQLite file.
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}

# DATABASE_URL looks like:  postgresql://USER:PASSWORD@HOST/DBNAME?sslmode=require
# dj_database_url.config() reads DATABASE_URL and turns it into Django's DATABASES dictionary.
if os.getenv("DATABASE_URL"):
    DATABASES = {
        "default": dj_database_url.config(
            conn_max_age=600,          # reuse connections for 10 minutes
            conn_health_checks=True,   # check a reused connection is still alive
        )
    }

# ---------------------------------------------------------------- static files
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"          # `collectstatic` copies all CSS/JS here
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"},
}

# ---------------------------------------------------------------- HTTPS behind Render's proxy
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
