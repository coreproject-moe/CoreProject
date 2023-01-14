from datetime import datetime

from core.utilities.CachedLimiterSession import CachedLimiterSession
from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from requests_cache import RedisCache
from requests_ratelimiter import RedisBucket

from django.db.models import F
from django.utils import timezone

from ...models import KitsuModel
from ..__logger__ import logger

session = CachedLimiterSession(
    per_minute=90,
    bucket_class=RedisBucket,
    backend=RedisCache(),
)


@db_periodic_task(crontab(minute="*/1"))
def refresh_kitsu_jwt() -> None:
    models = KitsuModel.objects.annotate(
        expiry_date=F("created_at") + F("expires_in")
    ).filter(expiry_date__lte=timezone.now())

    for object in models:
        # We are adding the timestamp as directed by kitsu
        # Essentially what we are doing is we are taking the datetime object and 1 month to it
        # expires_in = object.created_at + timezone.timedelta(seconds=object.expires_in)

        res = session.post(
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
            object.created_at = timezone.make_aware(
                datetime.utcfromtimestamp(data["created_at"])
            )

            logger.info(f"Refreshed Token | Kitsu : {object.user}")
            object.save()

        else:
            logger.error(
                f"Cannot Refresh Token | Kitsu : {object.user} | Reason : {res.text}"
            )
            object.delete()
