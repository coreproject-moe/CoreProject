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
COPY poetry.lock pyproject.toml /code

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

RUN apk add nodejs-current npm 

COPY . /code
RUN poetry shell

# Build tailwind CSS codes
RUN poe tailwind_install
RUN poe tailwind_build
COPY . /code

RUN apk del nodejs npm

RUN chmod +x /code/server_entrypoint.sh
RUN chmod +x /code/worker_entrypoint.sh
