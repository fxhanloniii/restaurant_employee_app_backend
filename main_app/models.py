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
    region = models.CharField(max_length=100, blank=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    image_url = models.URLField(blank=True)

class Message(models.Model):
    username = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class OutOfStockItem(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
