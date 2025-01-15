from typing import cast

from apps.anime.models import AnimeModel
from apps.api.auth import AuthBearer
from apps.episodes.models import EpisodeModel
from apps.episodes.models.episode_comment import EpisodeCommentModel
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ...decorator import recursionlimit
from ...schemas.episodes.episode_comment import (
    EpisodeCommentGETSchema,
    EpisodeCommentTreeGETSchema,
    EpisodeCommentTreePOSTSchema,
)

router = Router()


@recursionlimit(90000)
def get_nested_children(item: EpisodeCommentModel):
    _list = []
    _list.append(
        {
            "pk": item.pk,
            "user": str(item.user),
            "text": item.text,
            "created_at": item.created_at,
            "children": [get_nested_children(i)[0] for i in item.get_children()],
        }
    )
    return _list


@router.get(
    "/{int:anime_id}/episodes/{int:episode_number}/comments",
    response=list[EpisodeCommentTreeGETSchema],
)
def get_individual_anime_episode_comments(
    request: HttpRequest,
    anime_id: int,
    episode_number: int,
):
    query: list[EpisodeCommentModel] = get_list_or_404(
        get_object_or_404(
            AnimeModel,
            pk=anime_id,
        )
        .episodes.get(episode_number=episode_number)
        .episode_comments.all()
    )

    return_list = []

    while query:
        item = query.pop()
        return_list.extend(get_nested_children(item))

    return return_list


@router.post(
    "/{int:anime_id}/episodes/{int:episode_number}/comments",
    response=EpisodeCommentGETSchema,
    auth=AuthBearer(),
)
def post_individual_anime_episode_comment(
    request: HttpRequest,
    anime_id: int,
    episode_number: int,
    payload: EpisodeCommentTreePOSTSchema,
) -> EpisodeCommentModel:
    data = payload.dict(exclude_none=True, exclude_unset=True)

    comment_instance = EpisodeCommentModel.objects.create(
        text=data["text"],
        user=request.auth,
    )

    if parent_pk := data.get("parent_pk"):
        if parent_pk != 0:
            parent_instance = get_object_or_404(EpisodeCommentModel, pk=parent_pk)
            comment_instance.set_parent(parent_instance)

    query_object = get_object_or_404(
        get_object_or_404(
            AnimeModel,
            pk=anime_id,
        ).episodes,
        episode_number=episode_number,
    )
    query = cast(EpisodeModel, query_object)

    query.episode_comments.add(comment_instance)

    return comment_instance
