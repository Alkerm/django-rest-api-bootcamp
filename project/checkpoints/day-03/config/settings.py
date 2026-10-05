"""
Django settings for the Task Management API.

Tuwaiq Club at KFUPM - Building REST APIs with Django (Oct 11-15, 2026).
Created with `django-admin startproject config .` and cleaned up for the program.
"""
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent

# Development-only value - NOT a real secret.
# On Day 4 you will read SECRET_KEY, DEBUG and ALLOWED_HOSTS from environment variables.
SECRET_KEY = "development-only-key"
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    # TODO [Day 3 · P1]: Add DRF's token app so Django creates the token table.
    #   After saving, run:  python manage.py migrate   (you should see "authtoken" migrations apply)
    # HINT: days/day-03/hints.md#p1
    # YOUR CODE HERE
    "tasks",
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


# Database - local SQLite file (Days 1-4). PostgreSQL is added on Day 5.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


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

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Django REST Framework
# Authentication  = WHO is calling?          (token in the "Authorization: Token <key>" header)
# Permission      = WHAT may they do?        (only authenticated users)

REST_FRAMEWORK = {
    # TODO [Day 3 · P2]: Add "DEFAULT_AUTHENTICATION_CLASSES" with TWO classes, in this order:
    #   1. rest_framework.authentication.TokenAuthentication     -> used by API clients (Postman, tests)
    #   2. rest_framework.authentication.SessionAuthentication   -> keeps the browsable-API login working
    #   ORDER MATTERS: with TokenAuthentication first, a request without credentials gets 401 (not 403).
    # HINT: days/day-03/hints.md#p2
    # YOUR CODE HERE
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
