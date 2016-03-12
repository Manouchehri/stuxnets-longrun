import os
import logging

DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

SECRET = '\x00'*128
AUTH_SECRET = '\x00'*128

LOGGING_ENABLED = True
LOGGING_LEVEL = logging.INFO

celery = {
    'BROKER_URL': 'redis://localhost:6379/0',
    'CELERY_IMPORTS': ['minou2.analysis'],
    'CELERY_RESULT_BACKEND': 'redis://localhost:6379/1'
}

ALCHEMYAPI_TOKEN = '<Must be defined in env>'
if 'ALCHEMYAPI_TOKEN' in os.environ:
    ALCHEMYAPI_TOKEN = os.environ['ALCHEMYAPI_TOKEN']
