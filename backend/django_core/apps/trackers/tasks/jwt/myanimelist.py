from core.utilities.CachedLimiterSession import CachedLimiterSession
from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from requests_cache import RedisCache
from requests_ratelimiter import RedisBucket

from django.conf import settings
from django.db.models import F
from django.utils import timezone

from ...models import MalModel
from ..__logger__ import logger

session = CachedLimiterSession(
    per_minute=90,
    bucket_class=RedisBucket,
    backend=RedisCache(),
)


@db_periodic_task(crontab(minute="*/1"))
def refresh_mal_jwt() -> None:
    models = MalModel.objects.annotate(
        expiry_date=F("created_at") + F("expires_in")
    ).filter(expiry_date__lte=timezone.now())

    for object in models:
        # We are adding the timestamp as directed by kitsu
        # Essentially what we are doing is
        #  we are taking the datetime object and 1 month to it
        # expires_in = object.created_at + timezone.timedelta(seconds=object.expires_in)
        res = session.post(
            "https://myanimelist.net/v1/oauth2/token",
            data={
                "grant_type": "refresh_token",
                "client_id": settings.MAL_CLIENT_ID,
                "client_secret": settings.MAL_CLIENT_SECRET,
                "refresh_token": object.refresh_token,
            },
        )

        data = res.json()
        """
        The Data structure looks like this
            {
                "token_type":
                "expires_in":
                "access_token":
                "refresh_token":
            }
        """

        if res.status_code == 200:
            object.access_token = data["access_token"]
            object.expires_in = timezone.timedelta(seconds=data["expires_in"])
            object.refresh_token = data["refresh_token"]
            object.created_at = timezone.now()

            logger.info(f"Refreshed Token | MyAnimeList : {object.user}")
            object.save()

        else:
            logger.error(
                f"Cannot Refresh Token | MyAnimeList : {object.user} | Reason : {res.text}"
            )
            # object.delete()
