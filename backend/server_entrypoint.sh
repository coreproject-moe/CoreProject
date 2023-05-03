#!/bin/sh

until cd /code/django_core
do
    echo "Waiting for server volume..."
done

export PYTHONPATH=$PYTHONPATH:/code/django_core:/code


until (python manage.py makemigrations && python manage.py migrate)
do
    echo "Waiting for db to be ready..."
    sleep 2
done

python manage.py collectstatic --clear --link --no-input

# python manage.py createsuperuser --noinput
gunicorn core.asgi:application -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --access-logfile /code/logs/gunicorn.log --error-logfile - --user nobody

# for debug
#python manage.py runserver 0.0.0.0:8000
