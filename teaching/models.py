from django.core.files.storage import default_storage
from django.db import models

class Course(models.Model):
    slug = models.SlugField()
    abbreviation = models.CharField(max_length=10)
    title = models.CharField(max_length=80)

    def __unicode__(self):
        return u'{} ({})'.format(self.abbreviation, self.title)

class Offering(models.Model):
    def path(instance, filename):
        slug = instance.course.slug
        term = instance.term
        path = 'teaching/uwaterloo/{}/{}/{}'.format(slug, term, filename)
        default_storage.delete(path)
        return path

    course = models.ForeignKey(Course, related_name='offerings')
    term = models.PositiveSmallIntegerField()
    outline_file = models.FileField(blank=True, upload_to=path)
    midterm_file = models.FileField(blank=True, upload_to=path)
    final_file = models.FileField(blank=True, upload_to=path)

    def __unicode__(self):
        year = (1900 + self.term / 1000 * 100) + (self.term / 10  % 100)
        month = self.term % 10
        if month == 1:
            name = 'Winter'
        elif month == 5:
            name = 'Spring'
        elif month == 9:
            name = 'Fall'
        else:
            name = 'Unknown'
        return u'{}, {} {}'.format(unicode(self.course), name, year)

class Lecture(models.Model):
    def path(instance, filename):
        slug = instance.offering.course.slug
        term = instance.offering.term
        path = 'teaching/uwaterloo/{}/{}/lectures/{}'.format(slug, term,
                                                             filename)
        default_storage.delete(path)
        return path

    offering = models.ForeignKey(Offering, related_name='lectures')
    date = models.DateField()
    description = models.CharField(max_length=80)
    file = models.FileField(upload_to=path)

    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ['date']

class Assignment(models.Model):
    def path(instance, filename):
        slug = instance.offering.course.slug
        term = instance.offering.term
        path = 'teaching/uwaterloo/{}/{}/assignments/{}'.format(slug, term,
                                                                filename)
        default_storage.delete(path)
        return path

    offering = models.ForeignKey(Offering, related_name='assignments')
    date = models.DateField()
    description = models.CharField(max_length=80)
    file = models.FileField(upload_to=path)

    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ['date']
