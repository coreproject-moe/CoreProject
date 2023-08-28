from ..serializers.anime import AnimeSerializer
from apps.anime.models import AnimeModel

from rest_framework import generics
from ..bases.api_view import (
    SuperUserWriteProtectedAPIView,
    SuperUserUpdateProtectedAPIView,
)


class AnimeAPIView(
    SuperUserWriteProtectedAPIView,
    generics.ListCreateAPIView,
):
    queryset = AnimeModel.objects.all()
    serializer_class = AnimeSerializer


class AnimeSpecificAPIView(
    SuperUserUpdateProtectedAPIView,
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = AnimeModel.objects.all()
    serializer_class = AnimeSerializer
