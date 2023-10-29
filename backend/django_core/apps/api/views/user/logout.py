from django.http import HttpRequest
from rest_framework import status, views
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from typing import Any
from ...serializers.user.token import TokenSerializer


class LogoutAPIView(views.APIView):
    serializer_class = TokenSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self) -> dict[str, Any]:
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request: HttpRequest) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_token = serializer.validated_data["token"]

        token_instance = Token.objects.get(key=input_token)
        if token_instance.user == request.user:
            token_instance.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
