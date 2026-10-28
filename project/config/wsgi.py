"""
WSGI config for the Task Management API.

Gunicorn uses this module in production: `gunicorn config.wsgi:application`.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
