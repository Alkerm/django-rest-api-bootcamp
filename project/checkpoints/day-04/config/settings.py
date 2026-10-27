"""
Django settings for the Task Management API.

Tuwaiq Club at KFUPM - Building REST APIs with Django (Oct 25-29, 2026).
Created with `django-admin startproject config .` and cleaned up for the program.
"""
import os
from pathlib import Path

import dj_database_url
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuration that changes between your laptop and production comes from ENVIRONMENT VARIABLES.
# Locally nothing needs to be set: the defaults below are safe for development.
# In production (Render) you set: SECRET_KEY, DEBUG=False, ALLOWED_HOSTS=<your-app>.onrender.com
#
# TODO [Day 4 · P6]: Read the three settings from the environment with os.getenv(name, default):
#   SECRET_KEY     default "development-only-key"
#   DEBUG          default "True"  -> convert the TEXT to a bool: "true"/"True" -> True, anything else -> False
#   ALLOWED_HOSTS  default "127.0.0.1,localhost" -> split on "," into a list, strip spaces, drop empty items
# HINT: days/day-04/hints.md#p6  |  Example: days/day-04/example/settings_env.py
# YOUR CODE HERE - replace the placeholder lines below
SECRET_KEY = "development-only-key"
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# GIVEN (Day 5): Render sets RENDER=true on its servers. There DEBUG is False unless you set the DEBUG variable,
# so a forgotten variable can never publish error pages with your code and settings. Locally nothing changes.
if os.getenv("RENDER") and not os.getenv("DEBUG"):
    DEBUG = False

# Render terminates HTTPS and forwards CSRF-protected admin/login forms from your https:// URL.
# GIVEN: trusted https:// origins for the admin/login forms (comma-separated, from the environment).
CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]

# Safety net: never run production with the public development key.
if not DEBUG and SECRET_KEY == "development-only-key":
    raise ImproperlyConfigured("Set the SECRET_KEY environment variable when DEBUG is False.")

# Production-only HTTPS hardening (Render serves your app over HTTPS behind a proxy).
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    # TODO [Day 4 · P1]: Add DRF's token app so Django creates the token table.
    #   After saving, run:  python manage.py migrate   (you should see "authtoken" migrations apply)
    # HINT: days/day-04/hints.md#p1
    # YOUR CODE HERE
    "tasks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # GIVEN: WhiteNoise serves CSS/JS when DEBUG is False (must stay right after SecurityMiddleware).
    "whitenoise.middleware.WhiteNoiseMiddleware",
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


# Database
# Local default: SQLite file. Production: PostgreSQL on Neon, given as ONE connection string in DATABASE_URL.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# TODO [Day 5 · P1]: When the DATABASE_URL environment variable exists, replace DATABASES with
#   dj_database_url.config(conn_max_age=600, conn_health_checks=True).
#   Without DATABASE_URL, keep SQLite (so your laptop and the tests work without PostgreSQL).
# HINT: days/day-05/hints.md#p1  |  Example: days/day-05/example/settings_production.py
# YOUR CODE HERE


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# Riyadh time is used so "today" (for due-date validation) matches the participants' calendar.

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Riyadh"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"

# GIVEN: `collectstatic` gathers files into STATIC_ROOT and WhiteNoise serves them compressed.
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"},
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Django REST Framework
# Authentication  = WHO is calling?          (token in the "Authorization: Token <key>" header)
# Permission      = WHAT may they do?        (only authenticated users)

REST_FRAMEWORK = {
    # TODO [Day 4 · P2]: Add "DEFAULT_AUTHENTICATION_CLASSES" with TWO classes, in this order:
    #   1. rest_framework.authentication.TokenAuthentication     -> used by API clients (Postman, smoke test)
    #   2. rest_framework.authentication.SessionAuthentication   -> keeps the browsable-API login working
    #   ORDER MATTERS: with TokenAuthentication first, a request without credentials gets 401 (not 403).
    # HINT: days/day-04/hints.md#p2
    # YOUR CODE HERE
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
