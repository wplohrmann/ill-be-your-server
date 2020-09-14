from .io import try_get

url = "https://www.bbcgoodfood.com/search/recipes/?q=Pasta+recipes&sort=-relevance"

soup = try_get(url)

cards = soup.findAll("a", attrs={"class": "standard-card-new__article-title"})


