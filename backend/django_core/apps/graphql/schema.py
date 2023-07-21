import strawberry
import strawberry_django
from strawberry_django.permissions import IsSuperuser

from gqlauth.core.types_ import GQLAuthError, GQLAuthErrors
from gqlauth.core.utils import get_user
from gqlauth.user import arg_mutations as mutations
from strawberry.schema.config import StrawberryConfig
from strawberry_django.optimizer import DjangoOptimizerExtension
from strawberry.types import Info
from .mutations.anime import AnimeInput

from .types.anime import Anime
from .types.character import Character
from .types.producer import Producer
from .types.staff import Staff


@strawberry.type
class Query:
    animes: list[Anime] = strawberry_django.field(pagination=True)
    characters: list[Character] = strawberry_django.field(pagination=True)
    staffs: list[Staff] = strawberry_django.field(pagination=True)
    producers: list[Producer] = strawberry_django.field(pagination=True)


@strawberry.type
class Mutations:
    register = mutations.Register.field
    verify_account = mutations.VerifyAccount.field
    token_auth = mutations.ObtainJSONWebToken.field

    @strawberry.mutation
    def create_anime(self, data: AnimeInput) -> Anime:
        user = get_user(data)
        if not user.is_superuser:
            raise GQLAuthError(code=GQLAuthErrors.UNAUTHENTICATED)
        print(data)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutations,
    config=StrawberryConfig(auto_camel_case=False),
    extensions=[
        DjangoOptimizerExtension,
    ],
)
