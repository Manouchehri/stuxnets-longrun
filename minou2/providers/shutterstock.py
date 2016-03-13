import requests
from requests.auth import HTTPBasicAuth
from config import SHUTTERSTOCK_CLIENT, SHUTTERSTOCK_SECRET

SEARCH_URL = 'https://api.shutterstock.com/v2/images/search'

def fetch(concept):
    req = requests.get(SEARCH_URL, params={
        'query': concept['text'],
        'per_page': 10,
        'view': 'full'
    }, auth=(SHUTTERSTOCK_CLIENT, SHUTTERSTOCK_SECRET))

    return [{
        'id': i['id'],
        'preview': i['assets']['preview']['url']
    } for i in req.json()['data']]
