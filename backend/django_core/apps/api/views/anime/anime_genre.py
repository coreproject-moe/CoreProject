from http import HTTPStatus

from apps.anime.models import AnimeModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.api.auth import AuthBearer
from apps.user.models import CustomUser
from ninja import Router

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.anime.anime_genre import AnimeGenreGETSchema, AnimeGenrePOSTSchema

router = Router()


@router.get("/{int:anime_id}/genres", response=list[AnimeGenreGETSchema])
def get_individual_anime_genre_info(
    request: HttpRequest,
    anime_id: int,
) -> list[AnimeGenreModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).genres,
    )
    return query


@router.post("/{int:anime_id}/genres", response=AnimeGenreGETSchema, auth=AuthBearer())
def post_individual_anime_genre_info(
    request: HttpRequest,
    anime_id: int,
    payload: list[AnimeGenrePOSTSchema],
) -> list[AnimeGenreModel]:
    user: CustomUser = request.auth
    if not user.is_superuser:
        return HttpResponse(
            "Superuser is required for this operation", status=HTTPStatus.UNAUTHORIZED
        )

    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)
    instance_objects = []
    for object in payload:
        instance_objects.append(
            AnimeGenreModel(
                type="anime",
                **object.dict(exclude_none=True),
            )
        )

    instance = AnimeGenreModel.objects.bulk_create(instance_objects)
    anime_info_model.genres.add(instance)

    return instance
