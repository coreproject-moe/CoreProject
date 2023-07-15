import strawberry
from strawberry.schema.config import StrawberryConfig
import strawberry_django
from .types.anime import Anime
from .types.character import Character
from .types.producer import Producer
from .types.staff import Staff

from strawberry_django.optimizer import DjangoOptimizerExtension

from gqlauth.user import arg_mutations as mutations


@strawberry.type
class Query:
    animes: list[Anime] = strawberry_django.field(pagination=True)
    characters: list[Character] = strawberry_django.field(pagination=True)
    staffs: list[Staff] = strawberry_django.field(pagination=True)
    producers: list[Producer] = strawberry_django.field(pagination=True)


@strawberry.type
class Mutations:
    register = mutations.Register.field


schema = strawberry.Schema(
    query=Query,
    mutation=Mutations,
    config=StrawberryConfig(auto_camel_case=False),
    extensions=[
        DjangoOptimizerExtension,
    ],
)
