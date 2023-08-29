from apps.anime.models.anime_genre import AnimeGenreModel

from ...bases.api_view import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ...serializers.anime.genre import AnimeGenreSerializer


class AnimeGenresAPIView(ListCreateAPIView):
    queryset = AnimeGenreModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeGenreSerializer


class AnimeGenresSpecificAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AnimeGenreModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeGenreSerializer
