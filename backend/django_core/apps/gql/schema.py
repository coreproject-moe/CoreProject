import strawberry

from .types.anime import Anime
from .types.character import Character
from .types.producer import Producer
from .types.staff import Staff


@strawberry.type
class Query:
    animes: list[Anime] = strawberry.field(pagination=True)
    characters: list[Character] = strawberry.field(pagination=True)
    staffs: list[Staff] = strawberry.field(pagination=True)
    producers: list[Producer] = strawberry.field(pagination=True)


@strawberry.type
class Mutation: ...


schema = strawberry.Schema(query=Query, mutation=Mutation)
