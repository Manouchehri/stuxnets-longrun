#!/bin/bash
source venv/bin/activate
celery -A minou2 worker --loglevel=info
