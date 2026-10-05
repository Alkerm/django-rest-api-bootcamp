"""
Settings for the Day 5 exercise: Production readiness (PostgreSQL switch, static files, smoke test).

This exercise has its OWN database file: days/day-05/exercise/db.sqlite3 (created by `migrate`, not committed).
"""
import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "exercise-only-key")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ALLOWED_HOSTS = [host.strip() for host in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",") if host.strip()]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "catalog",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # TODO [Day 5 · Task 2a]: Add "whitenoise.middleware.WhiteNoiseMiddleware" on the line directly below
    #   SecurityMiddleware. It serves CSS/JS when DEBUG is False (Django itself stops serving them then).
    # HINT: days/day-05/hints.md#task-2
    # YOUR CODE HERE
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# TODO [Day 5 · Task 1]: If the environment variable DATABASE_URL is set, use it instead of the SQLite file:
#   DATABASES = {"default": dj_database_url.config(conn_max_age=600, conn_health_checks=True)}
#   If it is NOT set, keep the SQLite DATABASES above (local work and tests stay unchanged).
# HINT: days/day-05/hints.md#task-1  |  Example: days/day-05/example/settings_production.py
# YOUR CODE HERE

AUTH_PASSWORD_VALIDATORS = []  # exercise only: allow simple local passwords

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Riyadh"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

# TODO [Day 5 · Task 2b]: Configure collected static files:
#   STATIC_ROOT -> BASE_DIR / "staticfiles"     (where `collectstatic` copies every CSS/JS file)
#   STORAGES    -> {"default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
#                   "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"}}
# HINT: days/day-05/hints.md#task-2
# YOUR CODE HERE

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django REST Framework
# Every endpoint requires an authenticated user (token or browsable-API login).
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
