import os
import getpass
from unipath import FSPath as Path

PRODUCTION = 'http' == getpass.getuser()

ADMINS = (('Jon Eyolfson', 'jon@eyolfson.com'))
MANAGERS = ADMINS
TIME_ZONE = 'America/Toronto'

# settings_local should contain at least SECRET_KEY
from settings_local import *

USE_I18N = False
USE_L10N = False

BASE = Path(__file__).absolute().ancestor(1)
TEMPLATE_DIRS = [BASE.child('templates')]
MEDIA_ROOT = BASE.parent.child('media')

if PRODUCTION:
    DEBUG = False
    MEDIA_URL = "http://www.eyolfson.com/"
    ADMIN_MEDIA_PREFIX = "http://www.eyolfson.com/admin/"
else:
    DEBUG = True
    MEDIA_URL = "/media/"
    ADMIN_MEDIA_PREFIX = '/admin_media/'

SITE_ID = 1
ROOT_URLCONF = 'eyolfson_website.urls'

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
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
