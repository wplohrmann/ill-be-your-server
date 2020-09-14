import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

from ill_be_your_server.models import Recipe, RecipeURL

def parse_recipe(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
    else:
        return None
    soup = BeautifulSoup(html, features="lxml")
    recipe_dict = {}
    for tag in  soup.find_all(type="application/ld+json"):
        maybe_recipe = json.loads(tag.string)
        if maybe_recipe.get("@type"):
            if maybe_recipe["@type"] == "Recipe":
                recipe_dict["author"] = maybe_recipe.get("author", {"name": ""})["name"]
                recipe_dict["title"] = maybe_recipe.get("name", "Untitled")
                recipe_dict["source"] = url
                recipe_dict["date_added"] = datetime.now()
                recipe_dict["instructions"] = "\r\n".join(list(map(lambda x: x["text"], maybe_recipe["recipeInstructions"]))).replace("<p>", "").replace("<\p>", "")
                recipe_dict["ingredients"] = "\r\n".join(maybe_recipe["recipeIngredient"])

    recipe = Recipe(**recipe_dict)
    return recipe
