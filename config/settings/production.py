from .base import *
 
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEBUG = False

ALLOWED_HOSTS = ["95.217.222.90"]

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / "static"
