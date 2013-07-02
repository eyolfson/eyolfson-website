from django.db import models

class Project:
    slug = models.SlugField(max_length=50)
    url = models.URLField(max_length=200)
    description = models.TextField()

class AURProject:
    project = models.OneToOneField(Project)

class AURUpdate:
    package = models.SlugField(max_length=50)
    arch = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    updated = models.DateTimeField()
