from .base import *
 
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_USER_PASSWORD"],
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

DEBUG = False

# para la variable utilizar una cadena con espacios
ALLOWED_HOSTS = os.environ.get('SERVERNAMES').split(' ')

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / "static"

# Cofiguraciones para correo
# es necesario instalar mailutils y postfix
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'Soporte Técnico <info@pacamara.dev>'