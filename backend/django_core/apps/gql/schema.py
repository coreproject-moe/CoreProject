import strawberry
from typing import cast

import strawberry_django.permissions

from .mutations.anime import AnimeMutation
from .types.anime import AnimeType
from .types.character import Character
from .types.producer import Producer
from .types.staff import Staff
import strawberry_django
from strawberry.schema.config import StrawberryConfig
from .input.anime import AnimeInput

import strawberry_django


@strawberry.type
class Query:
    animes: list[AnimeType] = strawberry_django.field(pagination=True)
    characters: list[Character] = strawberry_django.field(pagination=True)
    staffs: list[Staff] = strawberry_django.field(pagination=True)
    producers: list[Producer] = strawberry_django.field(pagination=True)


@strawberry.type
class Mutation(AnimeMutation): ...


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=False),
)
