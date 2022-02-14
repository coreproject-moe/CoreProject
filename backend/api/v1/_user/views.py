from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.http.response import HttpResponse

# Create your views here.


class UserInfo(generics.ListAPIView):
    authentication_classes = [
        SessionAuthentication,
        JWTAuthentication,
    ]
    serializer_class = UserSerializer

    def get(self, request: HttpResponse):
        data = get_user_model().objects.get(id=request.user.id)
        serializer = UserSerializer(data, many=False)
        return Response(serializer.data)

    # def post(self, request: HttpResponse):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
