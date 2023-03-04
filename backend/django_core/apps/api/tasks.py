import asyncio
import os

from asgiref.sync import sync_to_async
from celery import shared_task
import httpx

from django.conf import settings
from django.core.files import File
from django.core.files.storage import FileSystemStorage

from ..episodes.models import EpisodeModel


async def post_files_to_streamsb(
    file: File,
):
    STREAMDB_SERVER_URL = "https://api.streamsb.com/api/upload/server"
    CLIENT = httpx.AsyncClient()

    server_url_res = await CLIENT.get(
        STREAMDB_SERVER_URL,
        params={
            "key": settings.STREAMSB_KEY,
        },
    )
    server_url_res_json = server_url_res.json()
    server_url = server_url_res_json["result"]

    file_res = await CLIENT.post(
        server_url,
        files={
            "file": file,
        },
        data={
            "api_key": settings.STREAMSB_KEY,
            "json": "1",
        },
    )
    file_code = file_res.json()["result"][0]["code"]
    return file_code


async def main(episode_model_instance: EpisodeModel, file: File):
    tasks = {
        "streamsb": post_files_to_streamsb(file=file),
    }
    results = await asyncio.gather(*tasks.values())
    episode_model_instance.providers = dict(zip(tasks, results))
    await sync_to_async(episode_model_instance.save)()


@shared_task()
def upload_file_to_providers(
    pk: int,
    file_name: str,
) -> None:
    instance = EpisodeModel.objects.get(pk=pk)
    file = FileSystemStorage().open(file_name)

    asyncio.run(main(instance, file))

    os.unlink(file.name)
