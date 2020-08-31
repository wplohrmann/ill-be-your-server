from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from urllib import parse
from .models import Recipe
from .forms import RecipeForm
import json
from django.http import HttpResponse

from .parsing import parse_recipe

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

def new_from_web(request):
    if request.method == "POST":
        url = request.POST["url"]
        maybe_recipe = parse_recipe(url)
        print(maybe_recipe)
        if maybe_recipe is not None:
            recipe_dict = {}
            recipe_dict["author"] = maybe_recipe.get("author", {"name": ""})["name"]
            recipe_dict["title"] = maybe_recipe.get("name", "Untitled")
            recipe_dict["source"] = url
            recipe_dict["instructions"] = "\r\n".join(list(map(lambda x: x["text"], maybe_recipe["recipeInstructions"]))).replace("<p>", "").replace("<\p>", "")
            recipe_dict["ingredients"] = "\r\n".join(maybe_recipe["recipeIngredient"])
            new_recipe = Recipe(**recipe_dict)
            new_recipe.save()

            return HttpResponse('Thanks! <a href="/recipes/">Back to main page</a>')
        else:
            return HttpResponse("Bad form!")


