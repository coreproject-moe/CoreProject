from rest_framework import views
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework import status
from ...serializers.user.username_validity import UsernameValiditySerializer
from apps.user.models import CustomUser

from typing import Any


class UsernameValiditiyAPIView(views.APIView):
    serializer_class = UsernameValiditySerializer

    def get_serializer_context(self) -> dict[str, Any]:
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request: HttpRequest) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]

        return (
            Response(status=status.HTTP_302_FOUND)
            if CustomUser.objects.filter(username=username).exists()
            else Response(status=status.HTTP_404_NOT_FOUND)
        )
