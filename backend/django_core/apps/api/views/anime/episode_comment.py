from apps.anime.models import AnimeModel
from apps.episodes.models.episode_comment import EpisodeCommentModel
from ninja import Router

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.episodes.episode_comment import (
    EpisodeCommentGETSchema,
    EpisodeCommentPOSTSchema,
)

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
        .episodes.get(episode_number__in=[episode_number])
        .episode_comments.all()
    )
    return query


@router.post(
    "/{int:anime_id}/episodes/{str:episode_number}/comments",
    response=EpisodeCommentGETSchema,
)
@login_required
def post_individual_anime_episode_comment(
    request: HttpRequest,
    anime_id: int,
    episode_number: str,
    payload: EpisodeCommentPOSTSchema,
) -> EpisodeCommentModel:
    data: EpisodeCommentModel = EpisodeCommentModel.objects.create(
        user=request.auth, **payload.dict()
    )

    AnimeModel.objects.get(pk=anime_id).episodes.get(
        episode_number__in=[episode_number]
    ).episode_comments.add(data)

    return data
