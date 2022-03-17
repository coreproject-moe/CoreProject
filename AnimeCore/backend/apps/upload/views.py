from pprint import pprint
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
from rest_framework.parsers import FormParser, MultiPartParser

from django.http.request import HttpRequest

from .models import AnimeInfoModel
from .serializers import AnimeInfoSerializer

# Create your views here.


class AnimeInfoView(generics.ListCreateAPIView):
    serializer_class = AnimeInfoSerializer

    def get(self, request: HttpRequest, pk: int) -> Response:
        data = AnimeInfoModel.objects.get(id=pk)
        serializer = self.get_serializer(data)
        return Response(serializer.data)
