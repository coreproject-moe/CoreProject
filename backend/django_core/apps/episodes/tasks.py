from celery import shared_task
import httpx

from django.conf import settings

from django.db.models import FileField
from .models import EpisodeModel


# Uploader functions


def post_files_to_streamsb(file: FileField) -> str:
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


def post_files_to_streamtape(name: str, file: FileField) -> str:
    """
    Create a new folder in Streamtape using the Streamtape API.
    Args:
    name (str): The name of the folder to be created.
    Returns:
    str: The ID of the newly created folder, or the ID of the parent folder if folder creation fails.
    Note:
    This function requires the following constants to be defined: LOGIN, KEY, and PARENT_FOLDER_ID.
    """
    client = httpx.Client(http2=True, timeout=300)

    # Create Folder
    url = "https://api.streamtape.com/file/createfolder"
    params = {
        "login": settings.STREAMTAPE_LOGIN,
        "key": settings.STREAMTAPE_KEY,
        "name": name,
        "pid": settings.STREAMTAPE_PARENT_FOLDER_ID,
    }
    response = client.get(url, params=params)
    if response.status_code == 200:
        folder_id_data = response.json()
        if result := folder_id_data["result"]:
            folder_id = result["folderid"]
        folder_id = settings.STREAMTAPE_PARENT_FOLDER_ID
    folder_id = settings.STREAMTAPE_PARENT_FOLDER_ID

    # Upload Server get
    url = "https://api.streamtape.com/file/ul"
    params = {
        "login": settings.STREAMTAPE_LOGIN,
        "key": settings.STREAMTAPE_KEY,
        "folder": folder_id,
    }
    response = client.get(url, params=params)
    if response.status_code == 200:
        upload_url = response.json()["result"]["url"]

    response = client.post(upload_url, files={"file1": file.open("rb")})
    if response.status_code == 200:
        return response.json()["result"]["id"]


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
            "streamtape": post_files_to_streamtape(instance.episode_name, episode_file),
        }

        instance.providers = data
        instance.episode_file.delete()
        instance.save()
