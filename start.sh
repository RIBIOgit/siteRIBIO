#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput || true
gunicorn core.wsgi:application --bind 0.0.0.0:8000