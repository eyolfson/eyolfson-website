from django.conf.urls import patterns, url
from django_publications import views

urlpatterns = patterns('',
   url(r'^(?P<slug>[-a-zA-Z0-9]+)/bibtex/$', views.bibtex, name='bibtex'),
)
