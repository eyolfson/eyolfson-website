from django.db import models

class Invitation(models.Model):
    confirmation_code = models.CharField(max_length=4, blank=False)
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
