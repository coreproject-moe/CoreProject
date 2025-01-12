#!/bin/sh

until cd /code
do
    echo "Waiting for server volume..."
done

mkdir -p /var/run/celery /var/log/celery
chown -R nobody:nogroup /var/run/celery /var/log/celery
chown -R nobody:nogroup /code/django_core/media

# run a worker :)
export PYTHONPATH=$PYTHONPATH:/code/django_core:/code

celery -A django_core.core worker -l info --uid=nobody --gid=nogroup
