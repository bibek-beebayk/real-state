from .base import *


SECRET_KEY = 'django-insecure-nljiwm+ia_pcp5^d5@gr*g3b2cq5i2yq@s7g$-urxk^8t1&k=g'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'real_state_db',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}


AUTH_PASSWORD_VALIDATORS = []


INSTALLED_APPS += ['debug_toolbar', 'django_extensions']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INTERNAL_IPS = ["127.0.0.1", ]

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'


CORS_ALLOWED_ORIGINS = (
    'http://localhost:3000',
    'http://127.0.0.1:3000',
)
