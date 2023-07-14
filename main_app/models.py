from django.db import models
# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=250)
    allergies = models.CharField(max_length=250)
    description = models.TextField()
    course = models.CharField(max_length=50)
    image_url = models.URLField(blank=True)

class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=250)
    description = models.TextField()
    image_url = models.URLField(blank=True)

class Wine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True)
