from celery import Celery
from . import celery_app

@celery_app.task
def analyze(text):
    return 0
