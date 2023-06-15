import strawberry
from .types import Anime


@strawberry.type
class Query:
    anime: list[Anime] = strawberry.django.field()


schema = strawberry.Schema(query=Query)
