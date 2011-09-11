from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import TemplateView

# from django.contrib.sitemaps import FlatPageSitemap
# from eyolfson_website.apps.blog.sitemap import BlogSitemap

admin.autodiscover()

# sitemaps = { 
#     'blog': BlogSitemap,
#     'flatpages': FlatPageSitemap,
# }

urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name="index.html")),
    (r'^admin/', include(admin.site.urls)),
    (r'^scc/', include('eyolfson_website.apps.scc.urls', namespace='scc', app_name='scc')),
    # (r'^blog/', include('eyolfson_website.apps.blog.urls')),
    # (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap',
    #  {'sitemaps': sitemaps}),
)
