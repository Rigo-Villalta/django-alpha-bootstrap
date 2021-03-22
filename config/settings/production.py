from config.settings.development import ALLOWED_HOSTS, DEBUG
import os

from .base import *

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]
