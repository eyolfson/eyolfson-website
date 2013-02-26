from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField()
    text = models.TextField()
    date_time = models.DateTimeField(default=datetime.now)
 
    def __unicode__(self):
        return self.title
