from strawberry.django.views import GraphQLView as StrawberryDjangoGraphQLView
from typing import Any
from django.http import HttpRequest, HttpResponse
from apps.user.models import CustomUser
from .models import Token

# Create your views here.


class GraphQLView(StrawberryDjangoGraphQLView):
    def get_user(self, request: HttpRequest) -> CustomUser | None:
        token = request.headers.get("Authorization", None)
        try:
            token_instance = Token.objects.get(token=token.split(" ")[-1])
            return token_instance.user

        except (Token.DoesNotExist, AttributeError):
            return None

    def get_context(self, request: HttpRequest, response: HttpResponse) -> Any:
        context = {"user": self.get_user(request), request: request, response: response}

        return context
