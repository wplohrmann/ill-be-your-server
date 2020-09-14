import requests
from bs4 import BeautifulSoup

def get(*args, **kwargs):
    response = requests.get(*args, **kwargs)
    return BeautifulSoup(response.text, features="lxml")

def try_get(*args, **kwargs):
    try:
        return get(*args, **kwargs)
    except Exception as e:
        print(e)
        import pdb; pdb.set_trace()
        print("Whoops!")

