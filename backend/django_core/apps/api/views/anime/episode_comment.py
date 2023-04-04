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
    "/{int:anime_id}/episodes/{int:episode_number}/comments",
    response=list[EpisodeCommentTreeSchema],
)
@recursionlimit(90000)
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
        .episodes.get(episode_number__in=[episode_number])
        .episode_comments.all()
    )

    return_list = []

    def get_nested_children(item: EpisodeCommentModel):
        
        __list__ = []
        __list__.append(
            {
                "pk": item.pk,
                "user": str(item.user),
                "text": item.text,
                "comment_added": item.comment_added,
                "children": [get_nested_children(i)[0] for i in item.get_children()],
            }
        )
        return __list__

    for item in query:
        return_list.extend(get_nested_children(item))

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
