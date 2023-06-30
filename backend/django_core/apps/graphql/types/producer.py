import strawberry_django
from apps.producers.models import ProducerModel
from ..filters.staff import StaffFilter
from strawberry import auto


@strawberry_django.type(ProducerModel, filters=StaffFilter)
class Producer:
    mal_id: int
    kitsu_id: int
    anilist_id: int

    name: str
    name_japanese: str

    established: auto
    about: str
