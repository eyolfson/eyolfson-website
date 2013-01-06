from django.core.files.storage import default_storage
from django.db import models

PUBLICATIONS_DIR = 'publications'

def publication_path(instance, extra=''):
    path = '{}/{}{}.pdf'.format('publications', instance.slug, extra)
    default_storage.delete(path)
    return path

def publication_paper_path(instance, filename):
    return publication_path(instance)

def publication_slides_path(instance, filename):
    return publication_path(instance, '-slides')

class Publication(models.Model):
    slug = models.SlugField()
    display = models.TextField()
    paper = models.FileField(blank=True, upload_to=publication_paper_path)
    slides = models.FileField(blank=True, upload_to=publication_slides_path)
    pub_date = models.DateTimeField(blank=True, null=True)
    bibtex = models.TextField()
