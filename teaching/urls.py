from django.conf.urls import patterns, url
from teaching.views import *

urlpatterns = patterns('',
   url(r'^$', home, name='home'),
)
