from .models import KitsuModel
from huey.contrib.djhuey import periodic_task
from huey import crontab
from datetime import datetime
import httpx
from django.utils import timezone


@periodic_task(crontab(minute="*/1"))
def refresh_kitsu_jwt():

    models = KitsuModel.objects.all()

    for object in models:
        expires_in = object.created_at + timezone.timedelta(seconds=object.expires_in)

        if timezone.now() > expires_in:
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
                object.expires_in = data["expires_in"]
                object.refresh_token = data["refresh_token"]
                object.created_at = datetime.fromtimestamp(data["created_at"])
                object.save()
            else:
                object.delete()

            print(f"Refreshed Token | Kitsu | {object.user}")
