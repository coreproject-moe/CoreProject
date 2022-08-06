from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ..models import AnimeInfoModel, EpisodeModel, EpisodeTimestampModel
from ..schemas import EpisodeTimestampGETSchema, EpisodeTimestampPOSTSchema

router = Router()


@router.get(
    "/info/{int:anime_id}/episodes/{str:episode_number}/timestamps",
    response=list[EpisodeTimestampGETSchema],
)
def get_individual_anime_episode_timestamp_info(
    request: HttpRequest, anime_id: int, episode_number: str
):
    query = get_list_or_404(
        get_object_or_404(AnimeInfoModel, pk=anime_id)
        .anime_episodes.get(episode_number__in=[episode_number])
        .episode_timestamps.all()
    )
    return query


@router.post(
    "/info/{int:anime_id}/episodes/{str:episode_number}/timestamps",
    response=EpisodeTimestampGETSchema,
)
def post_individual_anime_episode_timestamp_info(
    request: HttpRequest,
    anime_id: int,
    episode_number: str,
    payload: EpisodeTimestampPOSTSchema,
):
    data, created = EpisodeTimestampModel.objects.update_or_create(
        episode=EpisodeModel.objects.get(episode_number=episode_number),
        user=request.user,
        defaults={
            "timestamp": payload.dict().get("timestamp"),
        },
    )

    if created:
        AnimeInfoModel.objects.get(pk=anime_id).anime_episodes.get(
            episode_number=episode_number
        ).episode_timestamps.add(data)

    return data
