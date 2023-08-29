from apps.anime.models.anime_genre import AnimeGenreModel
from apps.api.permissions import IsSuperUserOrReadOnly
from rest_framework import generics

from ...serializers.anime.genre import AnimeGenreSerializer


class AnimeGenresAPIView(generics.ListCreateAPIView):
    queryset = AnimeGenreModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeGenreSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class AnimeGenresSpecificAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimeGenreModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeGenreSerializer
    permission_classes = (IsSuperUserOrReadOnly,)
