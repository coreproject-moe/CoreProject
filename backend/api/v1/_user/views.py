from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.http.response import HttpResponse
from django.contrib.auth import get_user_model

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

    def list(self, request: HttpResponse):
        data = get_user_model().objects.get(id=request.user.id)
        serializer = UserSerializer(data)
        return Response(serializer.data)
