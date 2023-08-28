from rest_framework.response import Response
from ..serializers.anime import AnimeSerializer
from apps.anime.models import AnimeModel

from rest_framework import generics
from typing import NoReturn
from ..bases.api_view import SuperUserWriteProtectedAPIView


class AnimeAPIView(generics.ListCreateAPIView, SuperUserWriteProtectedAPIView):
    queryset = AnimeModel.objects.all()
    serializer_class = AnimeSerializer


class AnimeSpecificAPIView(
    generics.RetrieveUpdateDestroyAPIView, SuperUserWriteProtectedAPIView
):
    queryset = AnimeModel.objects.all()
    serializer_class = AnimeSerializer
