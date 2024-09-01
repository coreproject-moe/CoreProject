from apps.user.models import CustomUser
import strawberry
from strawberry.schema.config import StrawberryConfig
import strawberry_django

from .mutations.anime import AnimeMutation
from .mutations.character import CharacterMutation
from .mutations.comment import CommentMutation
from .mutations.episode import EpisodeMutation
from .mutations.user import UserMutation
from .types.anime import AnimeType
from .types.character import CharacterType
from .types.comment import CommentType
from .types.producer import ProducerType
from .types.staff import StaffType
from .types.user import UserType


@strawberry.type
class Query:
    animes: list[AnimeType] = strawberry_django.field(pagination=True)
    characters: list[CharacterType] = strawberry_django.field(pagination=True)
    staffs: list[StaffType] = strawberry_django.field(pagination=True)
    producers: list[ProducerType] = strawberry_django.field(pagination=True)

    @strawberry_django.field()
    def user(self, info: strawberry.Info) -> UserType:
        return CustomUser.objects.get(pk=info.context["user"].pk)

    comments: list[CommentType] = strawberry_django.field(pagination=True)


@strawberry.type
class Mutation(
    AnimeMutation,
    UserMutation,
    CommentMutation,
    CharacterMutation,
    EpisodeMutation,
): ...


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=False),
)
