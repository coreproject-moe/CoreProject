from strawberry.django.views import GraphQLView as StrawberryDjangoGraphQLView
from typing import Any
from django.http import HttpRequest, HttpResponse
from apps.user.models import CustomUser
from django.shortcuts import aget_object_or_404
from apps.user.models import CustomUser
from functools import cached_property
from .models import Token
from collections import ChainMap

# Create your views here.


class AsyncGraphQLView(StrawberryDjangoGraphQLView):
    def get_user(self, request: HttpRequest) -> CustomUser | None:
        token = request.headers.get("Authorization", None)
        try:
            token_instance = Token.objects.get(token=token.split(" ")[-1])
            return token_instance.user

        except Token.DoesNotExist:
            return None

    def get_context(self, request: HttpRequest, response: HttpResponse) -> Any:
        context = {"user": self.get_user(request), request: request, response: response}

        return context
