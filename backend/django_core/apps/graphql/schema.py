import strawberry
from strawberry.schema.config import StrawberryConfig
from strawberry_django_plus import gql
from strawberry_django_plus.optimizer import DjangoOptimizerExtension

from .types.anime import Anime
from .types.character import Character
from .types.producer import Producer
from .types.staff import Staff

from .mutations.anime import AnimeModelInput
from strawberry_django_plus.permissions import IsSuperuser
from strawberry_django_plus.directives import SchemaDirectiveExtension


@gql.type
class Query:
    animes: list[Anime] = gql.django.field(pagination=True)
    characters: list[Character] = gql.django.field(pagination=True)
    staffs: list[Staff] = gql.django.field(pagination=True)
    producers: list[Producer] = gql.django.field(pagination=True)


@gql.type
class Mutation:
    create_anime: Anime = gql.django.create_mutation(
        AnimeModelInput,
        directives=[IsSuperuser()],
    )


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=False),
    extensions=[
        DjangoOptimizerExtension,
        SchemaDirectiveExtension,
    ],
)
