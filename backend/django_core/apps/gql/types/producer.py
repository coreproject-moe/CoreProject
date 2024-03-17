import strawberry
from apps.producers.models import ProducerModel
from strawberry import auto

from ..filters.producer import ProducerFilter


@strawberry.type(ProducerModel, filters=ProducerFilter)
class Producer:
    mal_id: int
    kitsu_id: int
    anilist_id: int

    name: str
    name_japanese: str

    established: auto
    about: str
