from http import HTTPStatus
from typing import AnyStr

from apps.anime.models import AnimeModel
from apps.api.auth import AuthBearer
from apps.episodes.models import EpisodeModel
from apps.user.models import CustomUser
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from ninja import File, Form, Router
from ninja.files import UploadedFile
from pydantic import Json

from apps.api.decorator import permission_required
from apps.api.permissions import IsSuperUser

from ...schemas.episodes import EpisodeGETSchema

router = Router()


@router.get("/{int:anime_id}/episodes", response=list[EpisodeGETSchema])
def get_individual_episodes(
    request: HttpRequest,
    anime_id: int,
) -> list[EpisodeModel]:
    try:
        query = (
            AnimeModel.objects.get(pk=anime_id).episodes.all().order_by("episode_number")
        )
    except (AnimeModel.DoesNotExist, EpisodeModel.DoesNotExist):
        return HttpResponse("Object does not exist")

    return query


@router.post("/{int:anime_id}/episodes", response=EpisodeGETSchema, auth=AuthBearer())
@permission_required([IsSuperUser])
def post_individual_episodes(
    request: HttpRequest,
    anime_id: int,
    episode_number: int = Form(...),
    episode_name: str = Form(...),
    episode_length: int = Form(...),
    episode_thumbnail: UploadedFile | None = File(default=None),
    episode_summary: str = Form(None),
    providers: Json[AnyStr] | None = Form(None),
) -> EpisodeModel:
    # Set this at top
    # Because if there is no anime_info_model with corresponding query
    # theres no point in continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)

    payload = {
        "episode_number": episode_number,
        "episode_name": episode_name,
        "episode_thumbnail": episode_thumbnail,
        "episode_summary": episode_summary,
        "episode_length": episode_length,
        "providers": providers,
    }

    instance = EpisodeModel.objects.create(
        **{key: value for key, value in payload.items() if value}
    )
    anime_info_model.episodes.add(instance)
    return instance


@router.get(
    "/{int:anime_id}/episodes/{int:episode_number}",
    response=EpisodeGETSchema,
)
def get_individual_episode(
    request: HttpRequest,
    anime_id: int,
    episode_number: int,
):
    instance = get_object_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).episodes, episode_number=episode_number
    )
    return instance


@router.patch(
    "/{int:anime_id}/episodes/{int:episode_number}",
    response=EpisodeGETSchema,
    auth=AuthBearer(),
)
@permission_required([IsSuperUser])
def patch_individual_episode_info(
    request: HttpRequest,
    anime_id: int,
    episode_number: int,
    episode_name: str = Form(...),
    episode_thumbnail: UploadedFile | None = File(default=None),
    episode_summary: str | None = Form(None),
    episode_length: int = Form(None),
    providers: Json[AnyStr] | None = Form(None),
):
    episode_instance = get_object_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).episodes,
        episode_number=episode_number,
    )
    validated_data = {
        "episode_name": episode_name,
        "episode_thumbnail": episode_thumbnail,
        "episode_summary": episode_summary,
        "episode_length": episode_length,
        "providers": providers,
    }

    for attr, value in validated_data.items():
        if value:
            setattr(episode_instance, attr, value)
    # These tasks are here for celery actually
    episode_instance.save()

    return episode_instance
