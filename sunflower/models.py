from django.db import models

# Create your models here.

class Flower(models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=64)
