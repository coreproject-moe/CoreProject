import strawberry
from typing import cast
import datetime

from apps.anime.models import AnimeModel
from .permissions import IsAuthenticated, IsSuperUser

from .types.anime import Anime
from .types.character import Character
from .types.producer import Producer
from .types.staff import Staff
import strawberry_django
from strawberry.schema.config import StrawberryConfig
from .mutations.anime import AnimeInput
from strawberry.file_uploads import Upload

import strawberry_django
from strawberry.types import Info


@strawberry.type
class Query:
    animes: list[Anime] = strawberry_django.field(pagination=True)
    characters: list[Character] = strawberry_django.field(pagination=True)
    staffs: list[Staff] = strawberry_django.field(pagination=True)
    producers: list[Producer] = strawberry_django.field(pagination=True)


@strawberry.type
class Mutation:
    @strawberry_django.mutations.create(
        handle_django_errors=True,
        permission_classes=[
            # IsSuperUser
        ],
    )
    def add_anime(self, info: Info, data: AnimeInput) -> Anime:
        return cast(Anime, AnimeModel.objects.first())


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=False),
)
