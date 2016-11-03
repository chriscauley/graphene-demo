from django.conf import settings
from django.db import models

class Animal(models.Model):
  name = models.CharField(max_length=32)
  genus = models.CharField(max_length=32)
  is_domesticated = models.BooleanField(default=False)
  user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True)
  __unicode__ = lambda self: self.name
