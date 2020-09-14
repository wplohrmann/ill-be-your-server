from peewee import Model, CharField, DateField, SqliteDatabase, ForeignKeyField, TextField

db = SqliteDatabase("recipes.db")

class RecipeURL(Model):
    url = CharField()

    class Meta:
        database = db

class Recipe(Model):
    author = CharField()
    title = CharField()
    source = CharField()
    instructions = TextField()
    ingredients = TextField()
    date_added = DateField()
    class Meta:
        database = db
