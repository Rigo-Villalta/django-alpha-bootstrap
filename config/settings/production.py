from .base import *

DEBUG = False

# para la variable utilizar una cadena con espacios
ALLOWED_HOSTS = os.environ.get('SERVERNAMES').split(' ')

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / "static"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_USER_PASSWORD"],
        "HOST": os.environ["DB_HOST"], # DB_HOST=127.0.0.1 if localhost
        "PORT": os.environ["DB_HOST"], # DB_PORT=5432 default postgresql
    }
}

# Cofiguraciones para correo
# es necesario instalar mailutils y postfix
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = os.environ.get('DEFAUL_FROM_EMAIL').split(' ')

# Logging para producción con problemas técnicos
LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'log.txt',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['file'],
            'level': 'WARNING',
        },
    },
}