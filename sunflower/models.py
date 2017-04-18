from django.db import models

# Create your models here.


class Garden(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(default="")


class Flower(models.Model):
    name = models.CharField(max_length=128, unique=True)
    color = models.CharField(max_length=64)
    description = models.TextField(default="")
    garden = models.ForeignKey(Garden, null=True, default=None, on_delete=models.CASCADE)
