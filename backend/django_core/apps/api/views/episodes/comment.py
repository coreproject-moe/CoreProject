from apps.api.auth import AuthBearer
from apps.episodes.models.episode_comment import EpisodeCommentModel
from ninja import Router

from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from ...schemas.episodes.episode_comment import (
    EpisodeCommentTreePOSTSchema,
    EpisodeCommentGETSchema,
    EpisodeCommentTreePATCHSchema,
)

router = Router()


@router.post(
    "/episodes/comment",
    response=EpisodeCommentGETSchema,
    auth=AuthBearer(),
)
def post_individual_anime_episode_comment(
    request: HttpRequest,
    payload: EpisodeCommentTreePOSTSchema,
) -> EpisodeCommentModel:
    data = payload.dict(exclude_none=True)

    comment_instance = EpisodeCommentModel.objects.create(
        text=data["text"],
        user=request.auth,
    )

    if parent_pk := data.get("parent_pk"):
        parent_instance = get_object_or_404(EpisodeCommentModel, pk=parent_pk)
        comment_instance.set_parent(parent_instance)

    return comment_instance


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
