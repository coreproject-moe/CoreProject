#!/bin/sh

python ./django_core/manage.py flush --no-input
python ./django_core/manage.py migrate

exec "$@"
