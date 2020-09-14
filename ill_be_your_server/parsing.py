import json
import requests
from bs4 import BeautifulSoup

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
