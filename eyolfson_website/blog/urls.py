from django.conf.urls.defaults import *

urlpatterns = patterns('eyolfson.apps.blog.views',
    url(r'^$', 
        view='post_index',
        name='blog_index'
    ),
    url(r'^(?P<year>\d{4})/$',
        view='post_year',
        name='blog_year'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        view='post_month',
        name='blog_month'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        view='post_day',
        name='blog_day'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        view='post_detail',
        name='blog_detail'
    ),

    (r'^(?P<year>\d{4})/(?P<month>\d{1})/$', 'post_redirect'),
    (r'^(?P<year>\d{4})/(?P<month>\d{1})/(?P<day>\d{1})/$', 'post_redirect'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1})/$', 'post_redirect'),
    (r'^(?P<year>\d{4})/(?P<month>\d{1})/(?P<day>\d{2})/$', 'post_redirect'),
    (r'^(?P<year>\d{4})/(?P<month>\d{1})/(?P<day>\d{1})/(?P<slug>[-\w]+)/$', 'post_redirect'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1})/(?P<slug>[-\w]+)/$', 'post_redirect'),
    (r'^(?P<year>\d{4})/(?P<month>\d{1})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'post_redirect'),
)
