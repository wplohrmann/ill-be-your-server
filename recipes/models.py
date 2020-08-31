from django.db import models

class Recipe(models.Model):
    instructions = models.TextField()
    ingredients = models.TextField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    source = models.URLField()

    def list_ingredients(self):
        ingredients = self.ingredients.split("\r\n")
        return list(filter(lambda x: len(x) > 0, ingredients))

    def list_instructions(self):
        instructions = self.instructions.split("\r\n")
        return list(filter(lambda x: len(x) > 0, instructions))

