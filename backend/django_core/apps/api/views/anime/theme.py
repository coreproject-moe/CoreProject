from apps.anime.models.anime_theme import AnimeThemeModel
from rest_framework import generics

from ...bases.api_view import (
    SuperUserUpdateProtectedAPIView,
    SuperUserWriteProtectedAPIView,
)
from ...serializers.anime.theme import AnimeThemeSerializer


class AnimeThemesAPIView(
    SuperUserWriteProtectedAPIView,
    generics.ListCreateAPIView,
):
    queryset = AnimeThemeModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeThemeSerializer


class AnimeThemesSpecificAPIView(
    SuperUserUpdateProtectedAPIView,
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = AnimeThemeModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeThemeSerializer
