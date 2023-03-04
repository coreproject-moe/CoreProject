from http import HTTPStatus
from apps.anime.models import AnimeModel
from apps.episodes.models import EpisodeModel
from ninja import Router, Form, File
from ninja.files import UploadedFile

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from apps.api.auth import AuthBearer
from apps.user.models import CustomUser
from ...schemas.episodes import EpisodeGETSchema

router = Router()


@router.get("/{int:anime_id}/episodes", response=list[EpisodeGETSchema])
def get_individual_episodes(
    request: HttpRequest,
    anime_id: int,
) -> list[EpisodeModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).episodes,
    )
    return query


@router.post("/{int:anime_id}/episodes", response=EpisodeGETSchema, auth=AuthBearer())
def post_individual_episodes(
    request: HttpRequest,
    episode_number: int = Form(...),
    episode_name: str = Form(...),
    episode_cover: UploadedFile | None = File(default=None),
    episode_summary: str = Form(...),
) -> EpisodeModel:
    user: CustomUser = request.auth
    if not user.is_superuser:
        raise HttpResponse(
            "Superuser is required for this operation",
            status=HTTPStatus.UNAUTHORIZED,
        )
    # Set this at top
    # Because if there is no anime_info_model with corresponding query
    # theres no point in continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)

    payload = {
        "episode_number": episode_number,
        "episode_name": episode_name,
        "episode_cover": episode_cover,
        "episode_summary": episode_summary,
    }

    query = EpisodeModel.objects.create(
        **{key: value for key, value in payload.items() if value}
    )

    instance: EpisodeModel = query[0]
    anime_info_model.studios.add(instance)

    return instance
