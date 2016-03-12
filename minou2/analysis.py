import config

from celery import Celery
from . import celery_app
from .alchemyapi import AlchemyAPI

alchemyapi = AlchemyAPI(config.ALCHEMYAPI_TOKEN)

@celery_app.task
def analyze(text):
    keywords = alchemyapi.keywords('text', text)
    return keywords
