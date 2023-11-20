FROM python:3.12-alpine AS development_build

# python:
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
# pip:
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
# poetry:
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'
ENV DEBUG=false

RUN pip install --no-cache-dir "poetry" && poetry --version

WORKDIR /code
# copy project
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-dev

RUN apk --no-cache add nodejs-current npm

COPY . /code
RUN poetry shell

# Build Frontend
RUN npm i
RUN npm run prod

# Cleanups
RUN poetry cache clear --all . --no-interaction
RUN npm cache clean --force
RUN pip install "pip-autoremove"
RUN pip-autoremove poetry "pip-autoremove" -y
RUN apk del nodejs npm

# Copy the final codes
RUN python django_core/manage.py collectstatic --clear --link --no-input
COPY . /code

# Remove test folders
RUN find . -type d -name 'test*' -exec rm -r {} +

RUN chmod +x /code/server_entrypoint.sh
RUN chmod +x /code/worker_entrypoint.sh
RUN chmod +x /code/beat_entrypoint.sh

RUN chmod +x /code/entrypoint.sh


CMD ["entrypoint.sh"]
