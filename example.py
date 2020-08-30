import requests
from bs4 import BeautifulSoup
import json

def parse_recipe(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
    else:
        return None
    soup = BeautifulSoup(html, features="lxml")
    for tag in  soup.find_all(type="application/ld+json"):
        maybe_recipe = json.loads(tag.string)
        if maybe_recipe.get("@type"):
            if maybe_recipe["@type"] == "Recipe":
                return maybe_recipe

if __name__ == "__main__":
    url = "https://www.bbcgoodfood.com/recipes/20minute-seafood-pasta"
    maybe_recipe = parse_recipe(url)
