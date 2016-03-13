#!/bin/bash
source venv/bin/activate
gunicorn -w 1 minou2.server:app --log-file=-
