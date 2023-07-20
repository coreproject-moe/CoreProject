import strawberry
from apps.producers.models import ProducerModel


@strawberry.django.filters.filter(ProducerModel, lookups=True)
class ProducerFilter:
    mal_id: int | None
    kitsu_id: int | None

    name: str | None
    name_japanese: str | None
