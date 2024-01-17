import os

from .base import *  # noqa: F403

DEBUG = False

STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa: F405

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE"),
        "NAME": os.environ.get("SQL_DATABASE"),
        "USER": os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
        "HOST": os.environ.get("SQL_HOST"),
        "PORT": os.environ.get("SQL_PORT"),
    }
}


def is_superuser(user):
    return user.is_superuser


SILKY_PYTHON_PROFILER = True  # Use built-in cProfile
SILKY_AUTHENTICATION = True  # User must login
SILKY_AUTHORISATION = True  # User must have permissions
SILKY_PERMISSIONS = is_superuser
