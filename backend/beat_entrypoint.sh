#!/bin/sh

until cd /code
do
    echo "Waiting for server volume..."
done

# run a worker :)
export PYTHONPATH=$PYTHONPATH:/code/django_core:/code

celery -A django_core.core beat -l info
