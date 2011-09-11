import os
import sys

here = os.path.dirname(__file__)
parent = os.path.dirname(here)
if parent not in sys.path:
    sys.path.append(parent)

os.environ['DJANGO_SETTINGS_MODULE'] = 'eyolfson_website.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
