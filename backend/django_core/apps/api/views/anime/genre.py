from apps.anime.models.anime_genre import AnimeGenreModel

from rest_framework import generics
from ...bases.api_view import (
    SuperUserWriteProtectedAPIView,
    SuperUserUpdateProtectedAPIView,
)
from ...serializers.anime.genre import AnimeGenreSerializer


class AnimeGenresAPIView(
    SuperUserWriteProtectedAPIView,
    generics.ListCreateAPIView,
):
    queryset = AnimeGenreModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeGenreSerializer


class AnimeGenresSpecificAPIView(
    SuperUserUpdateProtectedAPIView,
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = AnimeGenreModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeGenreSerializer
