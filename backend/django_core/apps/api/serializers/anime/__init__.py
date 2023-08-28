from rest_framework.fields import empty
from apps.anime.models import AnimeModel, AnimeNameSynonymModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_theme import AnimeThemeModel
from apps.characters.models import CharacterModel
from rest_framework import serializers

from ...bases.serializer import GetOrCreateSlugRelatedField
from .genre import AnimeGenreSerializer
from .theme import AnimeThemeSerializer
from ..character import CharacterSerializer


class AbstractBaseAnimeSerializer(serializers.ModelSerializer):
    name_synonyms = GetOrCreateSlugRelatedField(
        many=True,
        slug_field="name",
        required=False,
        queryset=AnimeNameSynonymModel.objects.all(),
    )

    class Meta:
        model = AnimeModel
        fields = "__all__"
        read_only_fields = ["is_locked"]


class AnimeGETSerializer(AbstractBaseAnimeSerializer):
    genres = AnimeGenreSerializer(many=True, read_only=True)
    themes = AnimeThemeSerializer(many=True, read_only=True)
    characters = CharacterSerializer(many=True, read_only=True)


class AnimePOSTSerializer(AbstractBaseAnimeSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        required=False,
        slug_field="mal_id",
        queryset=AnimeGenreModel.objects.all(),
    )
    themes = serializers.SlugRelatedField(
        many=True,
        required=False,
        slug_field="mal_id",
        queryset=AnimeThemeModel.objects.all(),
    )

    characters = serializers.SlugRelatedField(
        many=True,
        required=False,
        slug_field="mal_id",
        queryset=CharacterModel.objects.all(),
    )
