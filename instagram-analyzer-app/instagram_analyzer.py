import requests
from pandas import json_normalize
import pandas as pd

from keys import CLIENT_ID

def instagram_data(query):
    base_url = "https://api.instagram.com/v1"
    url = (f"{base_url}/tags/{query}/media/recent?client_id={CLIENT_ID}&count=30")
    print(url)

    page = requests.get(url)
    page_json = page.json()
    



