from django.db import models

class ArchLinuxArchitecture(models.Model):
    slug = models.SlugField()

    def __unicode__(self):
        return self.slug

class ArchLinuxPackage(models.Model):
    def path(instance, filename):
        return 'packages/archlinux/{}/{}'.format(instance.arch.slug, filename)

    arch = models.ForeignKey(ArchLinuxArchitecture)
    file = models.FileField(upload_to=path)

    def __unicode__(self):
        return self.file.url
