from apps.anime.models import AnimeModel
from apps.anime.models.anime_genre import AnimeGenreModel
from ninja import Router

from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.anime.anime_genre import AnimeGenreSchema

router = Router()


@router.get("/{int:anime_id}/genres", response=list[AnimeGenreSchema])
def get_individual_anime_genre_info(
    request: HttpRequest,
    anime_id: int,
) -> list[AnimeGenreModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).genres,
    )
    return query


@router.post("/{int:anime_id}/genres", response=AnimeGenreSchema)
def post_individual_anime_genre_info(
    request: HttpRequest,
    anime_id: int,
    payload: AnimeGenreSchema,
) -> AnimeGenreModel:
    # Set this at top
    # Because if there is no anime_info_model with corresponding query
    # theres no point in continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)

    # query is a tuple of ( QuerySet,bool )
    query = AnimeGenreModel.objects.get_or_create(
        **payload.dict(),
    )

    instance: AnimeGenreModel = query[0]
    anime_info_model.genres.add(instance)

    return instance
