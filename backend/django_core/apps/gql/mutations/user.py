import strawberry
from strawberry.types import Info
import strawberry_django

from ..input.user import UserLoginInput

from ..types.token import TokenType
from ..models import Token

from django.contrib.auth import authenticate as django_authenticate, login as django_login
from django.http.request import HttpRequest
from typing import cast


@strawberry.type
class UserMutation:
    @strawberry_django.mutation()
    def login(self, info: Info, data: UserLoginInput) -> TokenType | None:
        request: HttpRequest = cast(HttpRequest, info.context["request"])
        user = django_authenticate(request, username=data.username, password=data.password)
        if user is not None:
            django_login(request, user)
            token, _ = Token.objects.get_or_create(user=user.pk)
            return token
