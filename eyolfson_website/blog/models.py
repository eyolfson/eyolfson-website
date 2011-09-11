from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique_for_date='pub_date')
    body = models.TextField()
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.now)
    enable_comments = models.BooleanField(default=True)
 
    def __unicode__(self):
        return '%s - %s' % (self.pub_date.strftime('%Y-%m-%d'), self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('blog_detail', None, {
            'year': self.pub_date.strftime('%Y'),
            'month': self.pub_date.strftime('%m'),
            'day': self.pub_date.strftime('%d'),
            'slug': self.slug
        })
