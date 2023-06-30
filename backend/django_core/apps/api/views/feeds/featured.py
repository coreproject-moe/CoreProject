from django.http import HttpRequest
from ninja import Router

from ....anime.models import AnimeModel
from ...auth import OptionalAuthBearer
from ...schemas.anime import AnimeInfoGETSchema

router = Router()


@router.get("/", response=list[AnimeInfoGETSchema], auth=OptionalAuthBearer())
def get_featured_animes(request: HttpRequest) -> list[AnimeModel]:
    query = AnimeModel.objects.all().order_by("-updated")[:10]
    return query
