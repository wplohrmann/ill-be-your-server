from django.forms import ModelForm, Form
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
                "title",
                "author",
                "ingredients",
                "instructions",
                 ]

