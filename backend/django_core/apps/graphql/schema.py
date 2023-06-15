import strawberry
from strawberry.schema.config import StrawberryConfig
from strawberry_django_plus import gql
from strawberry_django_plus.optimizer import DjangoOptimizerExtension

from .types import Anime


@gql.type
class Query:
    animes: list[Anime] = gql.django.field()
    anime: Anime = gql.django.field()


@strawberry.type
class Mutation:
    pass


schema = strawberry.Schema(
    query=Query,
    config=StrawberryConfig(auto_camel_case=False),
    extensions=[
        # other extensions...
        DjangoOptimizerExtension,
    ],
)
