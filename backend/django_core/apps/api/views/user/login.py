from typing import Any
from rest_framework.authtoken import views as rest_framework_authtoken_views
from rest_framework.response import Response
from django.contrib.auth import login
from django.http import HttpRequest


class LoginAPIView(rest_framework_authtoken_views.ObtainAuthToken):
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            if user is not None:
                login(request, user)
                print(1)
        return super().post(request, *args, **kwargs)
