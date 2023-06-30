import strawberry_django
from apps.producers.models import ProducerModel
from strawberry import auto

from ..filters.staff import StaffFilter


@strawberry_django.type(ProducerModel, filters=StaffFilter)
class Producer:
    mal_id: int
    kitsu_id: int
    anilist_id: int

    name: str
    name_japanese: str

    established: auto
    about: str
