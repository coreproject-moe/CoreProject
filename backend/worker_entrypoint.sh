#!/bin/sh

until cd /code/django_core
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A core worker -l info
