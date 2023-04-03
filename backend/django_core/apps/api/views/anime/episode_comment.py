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
    query = get_list_or_404(
        get_object_or_404(
            AnimeModel,
            pk=anime_id,
        )
        .episodes.get(episode_number__in=[episode_number])
        .episode_comments.all()
    )
    new_query = []

    for i in query:
        print(i)
        print(i.tree)

    return []


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


data = [
    {"data": {"desc": "1"}},
    {
        "data": {"desc": "2"},
        "children": [
            {"data": {"desc": "21"}},
            {"data": {"desc": "22"}},
            {
                "data": {"desc": "23"},
                "children": [
                    {"data": {"desc": "231"}},
                ],
            },
            {"data": {"desc": "24"}},
        ],
    },
    {"data": {"desc": "3"}},
    {
        "data": {"desc": "4"},
        "children": [
            {"data": {"desc": "41"}},
        ],
    },
]
