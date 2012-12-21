from settings_local import *
import os

TIME_ZONE = 'America/Toronto'
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = False

SITE_ID = 1
ROOT_URLCONF = 'eyolfson_website.urls'
WSGI_APPLICATION = 'eyolfson_website.wsgi.application'

if PRODUCTION:
    DEBUG = False
    MEDIA_URL = 'http://www.eyolfson.com/media/'
    STATIC_URL = 'http://www.eyolfson.com/static/'
    ADMIN_MEDIA_PREFIX = 'http://www.eyolfson.com/static/admin/'
else:
    DEBUG = True
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
    ADMIN_MEDIA_PREFIX = '/static/admin/'
TEMPLATE_DEBUG = DEBUG

WEBSITE_DIR = os.path.dirname(__file__)
WEB_ROOT_DIR = os.path.join(os.path.split(WEBSITE_DIR)[0], 'web_root')

MEDIA_ROOT = os.path.join(WEB_ROOT_DIR, 'media')
STATIC_ROOT = os.path.join(WEB_ROOT_DIR, 'static')
FIXTURE_DIRS = (os.path.join(WEBSITE_DIR, 'fixtures'),)
STATICFILES_DIRS = (os.path.join(WEBSITE_DIR, 'static'),)
TEMPLATE_DIRS = (os.path.join(WEBSITE_DIR, 'templates'),)

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
)
