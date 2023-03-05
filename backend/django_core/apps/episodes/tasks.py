from celery import shared_task
import httpx

from django.conf import settings

from .models import EpisodeModel


# Uploader functions


def post_files_to_streamsb(file):
    STREAMDB_SERVER_URL = "https://api.streamsb.com/api/upload/server"
    CLIENT = httpx.Client(timeout=300, http2=True)
    server_url_res = CLIENT.get(
        STREAMDB_SERVER_URL,
        params={
            "key": settings.STREAMSB_KEY,
        },
    )
    server_url_res_json = server_url_res.json()
    server_url = server_url_res_json["result"]

    file_res = CLIENT.post(
        server_url,
        files={
            "file": file.open("rb"),
        },
        data={
            "api_key": settings.STREAMSB_KEY,
            "json": "1",
        },
    )
    file_res_json = file_res.json()
    file_code = file_res_json["result"][0]["code"]

    return file_code


# Create your tasks here


@shared_task()
def upload_file_to_providers_and_set_thumbnail(
    pk: int,
) -> None:
    instance = EpisodeModel.objects.get(pk=pk)

    # This check is necessary as Celery executes same task multiple times
    if episode_file := getattr(instance, "episode_file"):
        data = {
            "streamsb": post_files_to_streamsb(episode_file),
        }

        instance.providers = data
        instance.episode_file.delete()
        instance.save()
