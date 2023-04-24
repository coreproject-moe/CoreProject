#!/bin/sh

until cd /code/django_core
do
    echo "Waiting for server volume..."
done

mkdir -p /var/run/celery /var/log/celery
chown -R nobody:nogroup /var/run/celery /var/log/celery

# run a worker :)
celery -A core beat -l info --uid=nobody --gid=nogroup
