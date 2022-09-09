from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ..models import AnimeModel
from ..models.episode_comment import EpisodeCommentModel
from ..schemas.episode_comment import EpisodeCommentGETSchema, EpisodeCommentPOSTSchema

router = Router()


@router.get(
    "/{int:anime_id}/episodes/{str:episode_number}/comments",
    response=list[EpisodeCommentGETSchema],
)
def get_individual_anime_episode_comments(
    request: HttpRequest,
    anime_id: int,
    episode_number: str,
) -> list[EpisodeCommentModel]:
    query = get_list_or_404(
        get_object_or_404(
            AnimeModel,
            pk=anime_id,
        )
        .anime_episodes.get(episode_number__in=[episode_number])
        .episode_comments.all()
    )
    return query


@router.post(
    "/{int:anime_id}/episodes/{str:episode_number}/comments",
    response=EpisodeCommentGETSchema,
)
def post_individual_anime_episode_comment(
    request: HttpRequest,
    anime_id: int,
    episode_number: str,
    payload: EpisodeCommentPOSTSchema,
) -> EpisodeCommentModel:
    data: EpisodeCommentModel = EpisodeCommentModel.objects.create(
        user=request.user, **payload.dict()
    )

    AnimeModel.objects.get(pk=anime_id).anime_episodes.get(
        episode_number__in=[episode_number]
    ).episode_comments.add(data)

    return data
