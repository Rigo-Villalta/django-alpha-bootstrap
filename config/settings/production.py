from .base import *
 
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEBUG = False

# para la variable utilizar una cadena con espacios
ALLOWED_HOSTS = os.environ.get('SERVERNAMES').split(' ')

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / "static"
