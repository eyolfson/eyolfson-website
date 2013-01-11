from django.conf.urls import patterns, url
from packages.views import *

urlpatterns = patterns('',
   url(r'^$', home, name='home'),
)
