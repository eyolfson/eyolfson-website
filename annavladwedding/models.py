from django.db import models

class Invitation(models.Model):
    confirmation_code = models.CharField(max_length=4, blank=False,
                                         db_index=True)
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)

class Response(models.Model):
    invitation = models.ForeignKey(Invitation, related_name='responses')
    time = models.DateTimeField(auto_now_add=True)
