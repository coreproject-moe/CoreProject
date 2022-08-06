from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ..models import AnimeInfoModel, EpisodeModel
from ..schemas import EpisodePOSTSchema, EpisodeGETSchema

router = Router()


@router.get("/info/{int:anime_id}/episodes", response=list[EpisodeGETSchema])
def get_individual_anime_episodes(request, anime_id: int):
    query = get_list_or_404(
        get_object_or_404(AnimeInfoModel, id=anime_id).anime_episodes
    )
    return query


# I will work on this
# File upload is broken
# https://github.com/vitalik/django-ninja/issues/371
# https://django-ninja.rest-framework.com/tutorial/file-params/
@router.post("/info/{int:anime_id}/episodes", response=EpisodeGETSchema)
def post_individual_anime_episodes(request, anime_id: int, payload: EpisodePOSTSchema):
    # Set this at top
    # Because if there is no anime_info_model with corresponding query theres no point in  continuing
    anime_info_model = get_object_or_404(AnimeInfoModel, pk=anime_id)
    instance, created = EpisodeModel.objects.get_or_create(
        **payload.dict(),
    )
    anime_info_model.anime_studios.add(instance)

    return instance
