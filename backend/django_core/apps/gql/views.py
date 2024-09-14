import re
from functools import cached_property
from typing import Any

from apps.user.models import CustomUser
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest, HttpResponse
from strawberry.django.views import GraphQLView as StrawberryDjangoGraphQLView

from .models import Token

# Create your views here.
token_pattern = re.compile(r"^Bearer\s+(.+)$")


class GraphQLView(StrawberryDjangoGraphQLView):
    @cached_property
    def get_user(self) -> CustomUser | AnonymousUser:
        token = self.request.headers.get("Authorization", "")
        token_match = token_pattern.match(token)
        if token_match:
            try:
                token_instance = Token.objects.get(token=token_match.group(1))
                return token_instance.user
            except Token.DoesNotExist:
                return AnonymousUser
        else:
            return AnonymousUser

    def get_context(self, request: HttpRequest, response: HttpResponse) -> Any:
        context = {"user": self.get_user, "request": request, "response": response}
        return context
