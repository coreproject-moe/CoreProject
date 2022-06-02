import logging
from datetime import datetime

import httpx
import pytz
from django.db.models import F
from django.utils import timezone
from huey import crontab
from huey.contrib.djhuey import periodic_task

from ..models import KitsuModel

logger = logging.getLogger("huey")


@periodic_task(crontab(minute="*/1"))
def refresh_jwt():

    models = []
    mal_models = MalModel.objects.annotate(
        expiry_date=F("created_at") + F("expires_in")
    ).filter(expiry_date__lte=timezone.now())
    anilist_models = AnilistModel.objects.annotate(
        expiry_date=F("created_at") + F("expires_in")
    ).filter(expiry_date__lte=timezone.now())
    kitsu_models = KitsuModel.objects.annotate(
        expiry_date=F("created_at") + F("expires_in")
    ).filter(expiry_date__lte=timezone.now())
    models.extend(mal_models)
    models.extend(anilist_models)
    models.extend(kitsu_models)

    for object in models:
        # We are adding the timestamp as directed by kitsu
        # Essentially what we are doing is we are taking the datetime object and 1 month to it
        # expires_in = object.created_at + timezone.timedelta(seconds=object.expires_in)

        res = httpx.post(
            "https://kitsu.io/api/oauth/token",
            json={
                "grant_type": "refresh_token",
                "refresh_token": object.refresh_token,
            },
        )

        data = res.json()
        """
            The Data structure looks like this
            {
                "access_token":
                "token_type":
                "expires_in":
                "refresh_token":
                "scope":
                "created_at":
            }
        """

        if res.status_code == 200:
            object.access_token = data["access_token"]
            object.expires_in = timezone.timedelta(seconds=data["expires_in"])
            object.refresh_token = data["refresh_token"]
            object.created_at = datetime.fromtimestamp(
                data["created_at"], tzinfo=pytz.UTC
            )
            object.save()

        else:
            object.delete()

        logger.info(f"Refreshed Token | Kitsu | {object.user}")
