"""
Day 4 exercise - Task 2: print the settings Django actually loaded (GIVEN - do not edit).

Run:  python show_settings.py
Then set environment variables in the SAME terminal and run it again (see README, Task 2).
"""
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.conf import settings  # noqa: E402

secret_source = "environment" if os.getenv("SECRET_KEY") else "default"
print(f"SECRET_KEY    : {'*' * 8} (from {secret_source}, {len(settings.SECRET_KEY)} characters)")
print(f"DEBUG         : {settings.DEBUG!r}  ({type(settings.DEBUG).__name__})")
print(f"ALLOWED_HOSTS : {settings.ALLOWED_HOSTS!r}")
