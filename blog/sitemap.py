from datetime import datetime
from django.contrib.sitemaps import Sitemap
from eyolfson.apps.blog.models import Post

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.filter(pub_date__lte=datetime.now())
