import strawberry

import strawberry_django.permissions

from .mutations.user import UserMutation
from .mutations.anime import AnimeMutation
from .mutations.comment import CommentMutation
from .types.anime import AnimeType
from .types.character import Character
from .types.producer import Producer
from .types.staff import Staff
from .types.user import User
from .types.comment import Comment
import strawberry_django
from strawberry.schema.config import StrawberryConfig

from apps.user.models import CustomUser


@strawberry.type
class Query:
    animes: list[AnimeType] = strawberry_django.field(pagination=True)
    characters: list[Character] = strawberry_django.field(pagination=True)
    staffs: list[Staff] = strawberry_django.field(pagination=True)
    producers: list[Producer] = strawberry_django.field(pagination=True)

    @strawberry_django.field()
    def user(self, info: strawberry.Info) -> User:
        return CustomUser.objects.get(id=info.context["user"].id)

    comments: list[Comment] = strawberry_django.field(pagination=True)


@strawberry.type
class Mutation(AnimeMutation, UserMutation, CommentMutation): ...


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=False),
)
