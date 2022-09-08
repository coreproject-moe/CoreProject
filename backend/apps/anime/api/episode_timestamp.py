from django.db.models import Avg
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ..models import AnimeModel
from ..models.episode_timestamp import EpisodeTimestampModel
from ..schemas.episode_timestamp import (
    EpisodeTimestampGETSchema,
    EpisodeTimestampPOSTSchema,
    EpisodeTimestampTotalTimestampSchema,
)

router = Router()


@router.get(
    "/{int:anime_id}/episodes/{str:episode_number}/total_watchtime",
    response=EpisodeTimestampTotalTimestampSchema,
)
def get_individual_anime_episode_total_timestamp_info(
    request: HttpRequest,
    anime_id: int,
    episode_number: str,
) -> dict[str, str]:
    query = (
        get_object_or_404(AnimeModel, pk=anime_id)
        .anime_episodes.get(episode_number__in=[episode_number])
        .episode_timestamps.all()
        .aggregate(Avg("timestamp"))
    )
    return {"total_watchtime": query["timestamp__avg"]}


@router.get(
    "/{int:anime_id}/episodes/{str:episode_number}/timestamps",
    response=list[EpisodeTimestampGETSchema],
)
def get_individual_anime_episode_timestamp_info(
    request: HttpRequest,
    anime_id: int,
    episode_number: str,
) -> list[EpisodeTimestampModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id)
        .anime_episodes.get(episode_number__in=[episode_number])
        .episode_timestamps.filter(user=request.user)
    )
    return query


@router.post(
    "/{int:anime_id}/episodes/{str:episode_number}/timestamps",
    response=EpisodeTimestampGETSchema,
)
def post_individual_anime_episode_timestamp_info(
    request: HttpRequest,
    anime_id: int,
    episode_number: str,
    payload: EpisodeTimestampPOSTSchema,
) -> EpisodeTimestampModel:
    query = EpisodeTimestampModel.objects.update_or_create(
        episode__episode_number__in=[episode_number],
        user=request.user,
        defaults={
            "timestamp": payload.dict().get("timestamp"),
        },
    )
    
    data: EpisodeTimestampModel = query[0]
    created = query[1]

    if created:
        AnimeModel.objects.get(pk=anime_id).anime_episodes.get(
            episode_number=episode_number
        ).episode_timestamps.add(data)

    return data
