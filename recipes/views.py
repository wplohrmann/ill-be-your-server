from django.shortcuts import render, get_object_or_404
from urllib import parse
from .models import Recipe
from .forms import RecipeForm
import json
from django.http import HttpResponse

def index(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipes/index.html", context)

def detail(request, recipe_id):
    context = {"recipe": get_object_or_404(Recipe, pk=recipe_id)}
    return render(request, "recipes/detail.html", context)

def new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            new_recipe = Recipe(**form.cleaned_data)
            new_recipe.save()
            return HttpResponse('Thanks! <a href="/recipes/">Back to main page</a>')
        else:
            return HttpResponse("Bad form!")
    else:
        form = RecipeForm()
        return render(request, "recipes/new.html", {"form": form})
