from ..serializers.anime import AnimeSerializer
from apps.anime.models import AnimeModel
from apps.anime.models.anime_genre import AnimeGenreModel
from rest_framework import generics
from ..bases.api_view import (
    SuperUserWriteProtectedAPIView,
    SuperUserUpdateProtectedAPIView,
)
from ..serializers.anime.genre import AnimeGenreSerializer


class AnimeAPIView(
    SuperUserWriteProtectedAPIView,
    generics.ListCreateAPIView,
):
    queryset = AnimeModel.objects.all()
    serializer_class = AnimeSerializer


class AnimeGenresAPIView(
    SuperUserWriteProtectedAPIView,
    generics.ListCreateAPIView,
):
    queryset = AnimeGenreModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeGenreSerializer


class AnimeSpecificAPIView(
    SuperUserUpdateProtectedAPIView,
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = AnimeModel.objects.all()
    serializer_class = AnimeSerializer
