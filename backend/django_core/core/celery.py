import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

## Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Celery beat
app.conf.beat_schedule = {
    # Characters
    # ==========
    # Executes every Friday night at 12:00 a.m.
    "get-periodic-characters-every-friday-morning": {
        "task": "apps.characters.tasks.get_periodic_character",
        "schedule": crontab(hour=0, minute=00, day_of_week=5),
    },
    # Staffs / People
    # ==========
    # Executes every Friday night at 12:00 a.m.
    "get-periodic-staffs-every-friday-morning": {
        "task": "apps.staffs.tasks.get_periodic_staff",
        "schedule": crontab(hour=0, minute=00, day_of_week=5),
    },
    # Anime
    # ======
    # Genre
    "get-periodic-genres-every-friday-night": {
        "task": "apps.anime.tasks.get_periodic_anime_genres",
        "schedule": crontab(hour=0, minute=00, day_of_week=5),
    },
}

app.conf.timezone = "UTC"

app.conf.broker_url = BASE_REDIS_URL
