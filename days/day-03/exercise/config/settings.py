"""
Settings for the Day 3 exercise: Personal reading list (token auth, ownership, validation).

This exercise has its OWN database file: days/day-03/exercise/db.sqlite3 (created by `migrate`, not committed).
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "exercise-only-key"  # not a secret: local exercise only
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
    # TODO [Day 3 · Task 1a]: Install DRF's token app, then run  python manage.py migrate
    #   -> you should see "Applying authtoken.0001_initial... OK" (this creates the authtoken_token table)
    # HINT: days/day-03/hints.md#task-1
    # YOUR CODE HERE
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
    # TODO [Day 3 · Task 1b]: Add "DEFAULT_AUTHENTICATION_CLASSES" so requests are identified by
    #   1. rest_framework.authentication.TokenAuthentication    (FIRST -> missing credentials give 401)
    #   2. rest_framework.authentication.SessionAuthentication  (keeps the browsable API login working)
    # HINT: days/day-03/hints.md#task-1
    # YOUR CODE HERE
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
