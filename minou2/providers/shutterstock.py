import requests
from . import celery_app

SEARCH_URL = 'https://api.shutterstock.com/v2/images/search'

@celery_app.task
def fetch(concept):
    req = requests.get(SEARCH_URL, params={'query': concept['text']})
    return [{
        'id': i['id'],
        'preview': i['assets']['preview']['url']
    } for i in req.json()['data']]
