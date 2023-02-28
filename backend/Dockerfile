FROM python:3.11.2-alpine AS development_build


ENV DJANGO_ENV=${DJANGO_ENV}
  # python:
ENV  PYTHONFAULTHANDLER=1 
ENV  PYTHONUNBUFFERED=1 
ENV  PYTHONHASHSEED=random 
 # pip:
ENV  PIP_NO_CACHE_DIR=off 
ENV  PIP_DISABLE_PIP_VERSION_CHECK=on 
ENV  PIP_DEFAULT_TIMEOUT=100 
# poetry:
ENV  POETRY_VERSION=1.3.2
ENV  POETRY_VIRTUALENVS_CREATE=false 
ENV  POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN pip install "poetry==$POETRY_VERSION" && poetry --version

WORKDIR /code
# copy project
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /code
RUN poetry shell
RUN poe mksync
RUN poe sync 
RUN poe dev 

ENTRYPOINT python /django_core/manage.py runserver 0.0.0.0:8000