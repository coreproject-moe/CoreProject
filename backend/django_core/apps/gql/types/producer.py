from apps.producers.models import ProducerModel
from strawberry import auto
import strawberry_django

from ..filters.producer import ProducerFilter


@strawberry_django.type(ProducerModel, filters=ProducerFilter)
class ProducerType:
    mal_id: int
    kitsu_id: int
    anilist_id: int

    name: str
    name_japanese: str

    established: auto
    about: str
