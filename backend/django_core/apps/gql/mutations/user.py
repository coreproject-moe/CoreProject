import strawberry
from strawberry.types import Info
import strawberry_django
from ..input.user import UserLoginInput

from ..types.user import UserType


@strawberry.type
class UserMutation:
    @strawberry_django.mutation()
    def login(self, info: Info, data: UserLoginInput) -> UserType:
        pass
