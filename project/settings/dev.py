import os
from .base import BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'chackchackchackkouloukouloukoulou'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_URL = "localhost:8000"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

WSGI_APPLICATION = 'project.wsgi.application'


LOG_DATEFMT = '%Y-%m-%d %H:%M'
