from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from eyolfson_website import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^software/$', views.software, name='software'),
    url(r'^software/aur/', include('django_aur.urls')),
    url(r'^cv/$', views.cv, name='cv'),
    url(r'^teaching/', include('teaching.urls', namespace='teaching')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^annavladwedding/$', 'annavladwedding.views.home'),
)

if not settings.PRODUCTION:
    urlpatterns += patterns('django.views',
        url(r'^media/(?P<path>.*)', 'static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
