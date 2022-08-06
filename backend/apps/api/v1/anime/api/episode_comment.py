from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ..models import AnimeInfoModel, EpisodeCommentModel
from ..schemas import EpisodeCommentGETSchema, EpisodeCommentPOSTSchema

router = Router()


@router.get(
    "/info/{int:anime_id}/episodes/{str:episode_number}/comments",
    response=list[EpisodeCommentGETSchema],
)
def get_individual_anime_episode_comments(
    request: HttpRequest, anime_id: int, episode_number: str
):
    query = get_list_or_404(
        get_object_or_404(
            AnimeInfoModel,
            pk=anime_id,
        )
        .anime_episodes.get(episode_number__in=[episode_number])
        .episode_comments.all()
    )
    return query


@router.post(
    "/info/{int:anime_id}/episodes/{str:episode_number}/comments",
    response=EpisodeCommentGETSchema,
)
def post_individual_anime_episode_comment(
    request: HttpRequest,
    anime_id: int,
    episode_number: str,
    payload: EpisodeCommentPOSTSchema,
):
    data = EpisodeCommentModel.objects.create(user=request.user, **payload.dict())

    AnimeInfoModel.objects.get(pk=anime_id).anime_episodes.get(
        episode_number__in=[episode_number]
    ).episode_comments.add(data)

    return data
