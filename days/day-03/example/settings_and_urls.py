"""
Day 3 worked example - enabling DRF token authentication (two files shown together).
"""

# ---------------------------------------------------------------- config/settings.py
INSTALLED_APPS = [
    # ... django.contrib apps ...
    "rest_framework",
    "rest_framework.authtoken",   # 1) adds the authtoken_token table -> run `python manage.py migrate`
    "notes",
]

REST_FRAMEWORK = {
    # 2) HOW requests are identified. Order matters:
    #    the FIRST class decides the 401 response + "WWW-Authenticate: Token" header for anonymous requests.
    #    With SessionAuthentication first, anonymous requests would get 403 instead of 401.
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    # 3) WHO may call the API at all
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# ---------------------------------------------------------------- config/urls.py
# NOTE: import obtain_auth_token only after "rest_framework.authtoken" is in INSTALLED_APPS,
# otherwise Django stops with "Model class ...Token doesn't declare an explicit app_label".
from django.urls import include, path  # noqa: E402
from rest_framework.authtoken.views import obtain_auth_token  # noqa: E402

urlpatterns = [
    # 4) login endpoint: POST {"username": "...", "password": "..."} -> {"token": "..."}
    path("api/auth/token/", obtain_auth_token, name="api-token"),
    path("api/", include("notes.urls")),
]

# Using the token from any client:
#   GET /api/notes/
#   Authorization: Token <the 40-character key returned by the login endpoint>
#
# Tokens can also be created for a user from the command line:
#   python manage.py drf_create_token alice
