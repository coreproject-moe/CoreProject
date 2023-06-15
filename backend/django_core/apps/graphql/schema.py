import strawberry
from .types import Anime
from strawberry.schema.config import StrawberryConfig
from strawberry.django import auth
from strawberry_django_plus.optimizer import DjangoOptimizerExtension
from strawberry_django_plus import gql


@gql.type
class Query:
    anime: list[Anime] = gql.django.field()


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
