from django.http.request import HttpRequest
from django.contrib.auth import get_user_model
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_headers

from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer

# Create your views here.


class UserInfo(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
):
    """
    * Shows User Info.
    * Accpets User Info changes.
    """

    authentication_classes = [
        SessionAuthentication,
        JWTAuthentication,
    ]
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [
        FormParser,
        MultiPartParser,
    ]

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(
        vary_on_headers(
            "Authorization",
        )
    )
    def get(self, request: HttpRequest) -> Response:
        data = get_user_model().objects.get(id=request.user.id)
        serializer = UserSerializer(data)
        return Response(serializer.data)

    def post(self, request: HttpRequest) -> Response:
        instance = get_user_model().objects.get(id=request.user.id)
        serializer = UserSerializer(data=request.data, instance=instance)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
