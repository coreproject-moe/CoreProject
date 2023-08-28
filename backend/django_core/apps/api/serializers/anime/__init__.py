from apps.anime.models import AnimeModel, AnimeNameSynonymModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_theme import AnimeThemeModel
from rest_framework import serializers

from ...bases.serializer import GetOrCreateSlugRelatedField
from ..character import CharacterSerializer


class AnimeSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        required=False,
        slug_field="name",
        queryset=AnimeGenreModel.objects.all(),
    )
    themes = serializers.SlugRelatedField(
        many=True,
        required=False,
        slug_field="name",
        queryset=AnimeThemeModel.objects.all(),
    )
    name_synonyms = GetOrCreateSlugRelatedField(
        many=True,
        slug_field="name",
        required=False,
        queryset=AnimeNameSynonymModel.objects.all(),
    )
    characters = CharacterSerializer(many=True)

    class Meta:
        model = AnimeModel
        fields = "__all__"
        read_only_fields = ["is_locked"]
