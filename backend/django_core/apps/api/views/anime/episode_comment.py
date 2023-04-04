from apps.anime.models import AnimeModel
from apps.api.auth import AuthBearer
from apps.episodes.models.episode_comment import EpisodeCommentModel
from ninja import Router

from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.episodes.episode_comment import (
    EpisodeCommentGETSchema,
    EpisodeCommentPOSTSchema,
    EpisodeCommentTreeSchema,
)
from ...decorator import recursionlimit

router = Router()


@router.get(
    "/{int:anime_id}/episodes/{str:episode_number}/comments",
    response=list[EpisodeCommentTreeSchema],
)
def get_individual_anime_episode_comments(
    request: HttpRequest,
    anime_id: int,
    episode_number: str,
):
    query: list[EpisodeCommentModel] = get_list_or_404(
        get_object_or_404(
            AnimeModel,
            pk=anime_id,
        )
        .episodes.get(episode_number__in=[episode_number])
        .episode_comments.all()
    )

    return_list = []

    for item in query:
        stack = []
        stack.append(item)
        nested_children = []
        while stack:
            current_item = stack.pop()
            children = current_item.get_children()

            child_nodes = []
            for child in children:
                child_node = {
                    "user": str(child.user),
                    "text": child.text,
                    "comment_added": child.comment_added,
                    "children": [],
                }
                stack.append(child)
                child_nodes.append(child_node)

            current_node = {
                "user": str(current_item.user),
                "text": current_item.text,
                "comment_added": current_item.comment_added,
                "children": child_nodes,
            }
            nested_children.append(current_node)

        return_list.append(nested_children[0])

    return return_list


@router.post(
    "/{int:anime_id}/episodes/{str:episode_number}/comments",
    response=EpisodeCommentGETSchema,
    auth=AuthBearer(),
)
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
