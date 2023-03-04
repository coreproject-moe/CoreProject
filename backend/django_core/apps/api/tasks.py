import math

import httpx
from celery import shared_task

from ..episodes.models import EpisodeModel
from django.core.files.storage import FileSystemStorage


@shared_task()
def upload_file_to_streamsb(
    pk: int,
    file_name: str,
) -> None:
    instance = EpisodeModel.objects.get(pk=pk)
    file = FileSystemStorage.open(file_name)

    print(file)
