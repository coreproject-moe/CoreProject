from apps.anime.models.anime_theme import AnimeThemeModel

from ...bases.api_view import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ...serializers.anime.theme import AnimeThemeSerializer


class AnimeThemesAPIView(ListCreateAPIView):
    queryset = AnimeThemeModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeThemeSerializer


class AnimeThemesSpecificAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AnimeThemeModel.objects.filter(type__icontains="anime")
    serializer_class = AnimeThemeSerializer
