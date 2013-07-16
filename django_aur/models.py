from django.db import models

class Update(models.Model):
    package = models.SlugField(max_length=50, db_index=True)
    arch = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
