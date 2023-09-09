from .base import *
from .apps import *

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Third-party apps

INSTALLED_APPS += [
    "drf_spectacular"
]

# Services

INSTALLED_APPS += [
    "accounts"
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

AUTH_USER_MODEL = "accounts.User"

"""
Swagger settings
"""
SPECTACULAR_SETTINGS = {
    'TITLE': 'Blog Platform',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}