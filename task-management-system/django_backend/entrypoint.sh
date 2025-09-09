#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
# python3 manage.py collectstatic --noinput
python3 manage.py createsuperuser --noinput --username ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_EMAIL} --password ${DJANGO_SUPERUSER_PASSWORD}
sleep 8
python3 manage.py runserver 0.0.0.0:${DJANGO_PORT}