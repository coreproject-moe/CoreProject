from apps.anime.models.anime_theme import AnimeThemeModel
from apps.api.permissions import IsSuperUserOrReadOnly
from rest_framework import generics

from ...serializers.anime.theme import AnimeThemeSerializer


class AnimeThemesAPIView(generics.ListCreateAPIView):
    queryset = AnimeThemeModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeThemeSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class AnimeThemesSpecificAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimeThemeModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeThemeSerializer
    permission_classes = (IsSuperUserOrReadOnly,)
