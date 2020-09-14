import os
from ill_be_your_server.io import try_get, get
from ill_be_your_server.models import RecipeURL, Recipe
from peewee import SqliteDatabase
import shutil
from ill_be_your_server.parsing import parse_recipe

db_path = "recipes.db"

if os.path.exists(db_path):
    shutil.rmtree(db_path)

db = SqliteDatabase(db_path)

db.connect()
db.create_tables([RecipeURL, Recipe])

base_url = "https://www.bbcgoodfood.com"
i = 1
while True:
    url = os.path.join(base_url, f"search/recipes/page/{i}?&sort=-date")
    print(url)

    soup = get(url)

    cards = soup.findAll("a", attrs={"class": "standard-card-new__article-title"})
    if len(cards) == 0:
        break

    for card in cards:
        relative_url = card["href"]
        recipe_url = base_url + relative_url
        RecipeURL.create(url=recipe_url).save()
        parse_recipe(recipe_url).save()
    i += 1
