# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CONTRIB_APPS = [
]

PROJECT_APPS = [
    'reservations',
]

INSTALLED_APPS = DJANGO_APPS + CONTRIB_APPS + PROJECT_APPS
