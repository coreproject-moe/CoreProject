from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router
from django.http import HttpRequest

from ..models import AnimeInfoModel, AnimeGenreModel
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
    instance, created = AnimeGenreModel.objects.get_or_create(
        **payload.dict(),
    )
    AnimeInfoModel.objects.get(pk=anime_id).anime_genres.add(instance)
    return instance
