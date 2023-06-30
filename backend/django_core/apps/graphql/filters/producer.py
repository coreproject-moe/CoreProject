import strawberry
from apps.producers.models import ProducerModel


@strawberry.django.filters.filter(ProducerModel, lookups=True)
class ProducerFilter:
    mal_id: int
    kitsu_id: int

    name: str
    name_japanese: str
