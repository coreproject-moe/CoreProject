from apps.anime.models.anime_genre import AnimeGenreModel

from rest_framework import serializers


class AnimeGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeGenreModel
        fields = ["mal_id", "name", "type", "description"]
