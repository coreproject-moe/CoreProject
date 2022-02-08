from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import (
    UserSerializer,
)

# Create your views here.


class UserInfo(APIView):
    authentication_classes = [
        JWTAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]

    def get(self, request):
        print(request.user)
        data = get_user_model().objects.get(id=request.user.id)
        serializer = UserSerializer(data, many=False)
        return Response(serializer.data)
