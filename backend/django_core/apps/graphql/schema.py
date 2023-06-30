import strawberry
from strawberry.schema.config import StrawberryConfig
from strawberry_django_plus import gql
from strawberry_django_plus.optimizer import DjangoOptimizerExtension

from .types.anime import Anime
from .types.character import Character
from .types.producer import Producer
from .types.staff import Staff


@gql.type
class Query:
    animes: list[Anime] = gql.django.field(pagination=True)
    characters: list[Character] = gql.django.field(pagination=True)
    staffs: list[Staff] = gql.django.field(pagination=True)
    producers: list[Producer] = gql.django.field(pagination=True)


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
