from django.db import models

class Recipe(models.Model):
    instructions = models.TextField()
    ingredients = models.TextField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    source = models.URLField()

