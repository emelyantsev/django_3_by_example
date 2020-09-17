from .base import *

DEBUG = False

ADMINS = (
('Aleksey E', 'aleks.twin@gmail.com'),
)

ALLOWED_HOSTS = ['.educaproject5.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'aleksey',
        'PASSWORD': '1234',
        'HOST': '172.17.236.91',
        'PORT': 5432
    }
}

# SSL config
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True