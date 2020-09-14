import requests
from bs4 import BeautifulSoup

def try_get(*args, **kwargs):
    try:
        response = requests.get(*args, **kwargs)
        return BeautifulSoup(response)
    except:
        import pdb; pdb.set_trace()
        print("Whoops!")

