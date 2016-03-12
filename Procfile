web: gunicorn -w 1 minou2.server:app --log-file=-
worker: celery -A minou2 worker --loglevel=info
redis: redis-server
