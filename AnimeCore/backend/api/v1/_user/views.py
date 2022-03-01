from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import get_user_model
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_headers

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


from .serializers import UserSerializer

# Create your views here.


class UserInfo(generics.ListAPIView):
    """
    Shows User Info.
    """

    authentication_classes = [
        SessionAuthentication,
        JWTAuthentication,
    ]
    serializer_class = [UserSerializer]
    permission_classes = [IsAuthenticated]

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
