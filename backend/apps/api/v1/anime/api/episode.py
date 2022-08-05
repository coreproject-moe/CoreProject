from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ..models import AnimeInfoModel
from ..schemas import EpisodeSchema

router = Router()


@router.get("/info/{int:anime_id}/episodes", response=list[EpisodeSchema])
def get_individual_anime_episodes(request, anime_id: int):
    query = get_list_or_404(
        get_object_or_404(AnimeInfoModel, id=anime_id).anime_episodes
    )
    return query
