from apps.anime.models.anime_theme import AnimeThemeModel
from rest_framework import serializers


class AnimeThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeThemeModel
        fields = ["mal_id", "name", "type", "description"]
