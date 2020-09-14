import requests
from bs4 import BeautifulSoup

url = "https://www.bbcgoodfood.com/search/recipes/?q=Pasta+recipes&sort=-relevance"

response = requests.get(url)
soup = BeautifulSoup(response.text)

cards = soup.findAll("a", attrs={"class": "standard-card-new__article-title"})


