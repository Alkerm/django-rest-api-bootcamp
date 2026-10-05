"""
Settings for the Day 4 exercise: Testing the reading-list API + configuration from environment variables.

This exercise has its OWN database file: days/day-04/exercise/db.sqlite3 (created by `migrate`, not committed).
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# TODO [Day 4 · Task 2a]: Read these three settings from ENVIRONMENT VARIABLES with os.getenv(name, default).
#   variable        default (used when the variable is not set)    type in Python
#   SECRET_KEY      "exercise-only-key"                            str
#   DEBUG           "True"                                         bool  -> True only when the text is "true" (any case)
#   ALLOWED_HOSTS   "127.0.0.1,localhost"                          list  -> split on ",", strip spaces, skip empty items
# HINT: days/day-04/hints.md#task-2  |  Example: days/day-04/example/settings_env.py
# YOUR CODE HERE
SECRET_KEY = "exercise-only-key"
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

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

AUTH_PASSWORD_VALIDATORS = []  # exercise only: allow simple local passwords

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Riyadh"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django REST Framework
# Day 3: every endpoint requires an authenticated user (GIVEN below).
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
