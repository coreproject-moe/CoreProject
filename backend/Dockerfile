FROM python:3.11.2-alpine AS development_build


# python:
ENV  PYTHONFAULTHANDLER=1
ENV  PYTHONUNBUFFERED=1
ENV  PYTHONHASHSEED=random
# pip:
ENV  PIP_NO_CACHE_DIR=off
ENV  PIP_DISABLE_PIP_VERSION_CHECK=on
ENV  PIP_DEFAULT_TIMEOUT=100
# poetry:
ENV  POETRY_VIRTUALENVS_CREATE=false
ENV  POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN pip install --no-cache-dir "poetry" && poetry --version

WORKDIR /code
# copy project
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

RUN apk --no-cache add nodejs-current npm

COPY . /code
RUN poetry shell

# Build tailwind CSS codes
RUN python django_core/manage.py tailwind install
RUN python django_core/manage.py tailwind build
RUN python django_core/manage.py collectstatic --clear --link --no-input
COPY . /code

RUN apk del nodejs npm

RUN chmod +x /code/server_entrypoint.sh
RUN chmod +x /code/worker_entrypoint.sh

RUN chmod +x /code/entrypoint.sh


CMD ["entrypoint.sh"]
