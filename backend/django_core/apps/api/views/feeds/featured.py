from ninja import Router

from django.http import HttpRequest

from ....anime.models import AnimeModel
from ...auth import AuthBearer
from ...schemas.anime import AnimeInfoGETSchema

router = Router()


@router.get("/", response=list[AnimeInfoGETSchema], auth=AuthBearer())
def get_featured_animes(request: HttpRequest) -> list[AnimeModel]:
    query = AnimeModel.objects.all().order_by("-updated")[:10]
    return query
