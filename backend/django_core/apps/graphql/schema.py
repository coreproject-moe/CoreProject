import strawberry
from strawberry.schema.config import StrawberryConfig

from .types import Anime


@strawberry.type
class Query:
    anime: list[Anime] = strawberry.django.field()


@strawberry.type
class Mutation:
    pass


schema = strawberry.Schema(query=Query, config=StrawberryConfig(auto_camel_case=False))
