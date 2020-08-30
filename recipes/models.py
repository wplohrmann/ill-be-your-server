from django.db import models

class Recipe(models.Model):
    instructions = models.TextField()
    ingredients = models.JSONField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    source = models.URLField()

