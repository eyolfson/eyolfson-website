from django.conf.urls import patterns, url
from django_publications import views

urlpatterns = patterns('',
   url(r'^(?P<slug>\w+)/bibtex/$', views.bibtex, name='bibtex'),
)
