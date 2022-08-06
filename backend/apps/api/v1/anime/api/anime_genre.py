from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ..models import AnimeGenreModel, AnimeInfoModel
from ..schemas import AnimeGenreSchema

router = Router()


@router.get("/info/{int:anime_id}/genres", response=list[AnimeGenreSchema])
def get_individual_anime_genre_info(request: HttpRequest, anime_id: int):
    query = get_list_or_404(get_object_or_404(AnimeInfoModel, id=anime_id).anime_genres)
    return query


@router.post("/info/{int:anime_id}/genres", response=AnimeGenreSchema)
def post_individual_anime_genre_info(
    request: HttpRequest, anime_id: int, payload: AnimeGenreSchema
):
    # Set this at top
    # Because if there is no anime_info_model with corresponding query theres no point in  continuing
    anime_info_model = get_object_or_404(AnimeInfoModel, pk=anime_id)

    instance, created = AnimeGenreModel.objects.get_or_create(
        **payload.dict(),
    )
    anime_info_model.anime_genres.add(instance)

    return instance
