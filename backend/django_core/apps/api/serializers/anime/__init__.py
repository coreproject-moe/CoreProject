from apps.anime.models import AnimeModel

from rest_framework import serializers
from .genre import AnimeGenreSerializer
from .theme import AnimeThemeSerializer


class AnimeSerializer(serializers.ModelSerializer):
    genres = AnimeGenreSerializer(many=True)
    themes = AnimeThemeSerializer(many=True)
    name_synonyms = serializers.StringRelatedField(many=True)

    class Meta:
        model = AnimeModel
        fields = "__all__"
        read_only_fields = ["is_locked"]
