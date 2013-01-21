from settings_local import *
import os

TIME_ZONE = 'America/Toronto'
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = False

SITE_ID = 1
ROOT_URLCONF = 'eyolfson_website.urls'
WSGI_APPLICATION = 'eyolfson_website.wsgi.application'

WEBSITE_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(WEBSITE_DIR)
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

if PRODUCTION:
    DEBUG = False
    MEDIA_ROOT = '/srv/http/eyolfson.com/media/'
    MEDIA_URL = 'https://eyolfson.com/media/'
    STATIC_ROOT = '/srv/http/eyolfson.com/static/'
    STATIC_URL = 'https://eyolfson.com/static/'
else:
    DEBUG = True
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
    STATIC_ROOT = ''
    STATIC_URL = '/static/'
TEMPLATE_DEBUG = DEBUG

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'publications',
    'teaching',
)
