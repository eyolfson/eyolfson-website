from django.conf.urls import patterns, url
from django_aur import views

urlpatterns = patterns('',
   url(r'^$', views.aur, name='aur'),
)
