from apps.api.auth import AuthBearer
from apps.episodes.models.episode_comment import EpisodeCommentModel
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router

from ...schemas.episodes.episode_comment import (
    EpisodeCommentGETSchema,
    EpisodeCommentTreePATCHSchema,
)

router = Router()


@router.patch(
    "/episodes/comment",
    response=EpisodeCommentGETSchema,
    auth=AuthBearer(),
)
def patch_individual_anime_episode_comment(
    request: HttpRequest,
    payload: EpisodeCommentTreePATCHSchema,
) -> EpisodeCommentModel:
    data = payload.dict(exclude_none=True)
    instance = get_object_or_404(EpisodeCommentModel, pk=data["pk"])
    if instance.user == request.auth:
        for attribute, value in data.items():
            setattr(instance, attribute, value)

        instance.save()

    return instance
