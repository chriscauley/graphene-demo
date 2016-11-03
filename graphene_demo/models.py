from django.db import models

class Animal(models.Model):
  name = models.CharField(max_length=32)
  genus = models.CharField(max_length=32)
  is_domesticated = models.BooleanField(default=False)
