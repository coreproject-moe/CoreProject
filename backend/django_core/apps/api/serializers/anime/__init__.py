from apps.anime.models import AnimeModel, AnimeNameSynonymModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_theme import AnimeThemeModel
from apps.characters.models import CharacterModel
from rest_framework import serializers

from ...bases.serializer import GetOrCreateSlugRelatedField
from ..character import CharacterSerializer
from .genre import AnimeGenreSerializer


class AnimeSerializer(serializers.ModelSerializer):
    genres = AnimeGenreSerializer(many=True, required=False)
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
    characters = CharacterSerializer(
        many=True,
        required=False,
    )

    class Meta:
        model = AnimeModel
        fields = "__all__"
        read_only_fields = ["is_locked"]

    def create(self, validated_data):
        # Anime specific data
        genres_data = validated_data.pop("genres")
        character_data = validated_data.pop("characters")

        instance = AnimeModel.objects.create(**validated_data)

        if character_data:
            for character in character_data:
                character_instance = CharacterModel.objects.get(mal_id=character["mal_id"])
                instance.characters.add(character_instance)

        if genres_data:
            for genre in genres_data:
                genre_instance = AnimeGenreModel.objects.get(mal_id=genre["mal_id"])
                instance.genres.add(genre_instance)

        instance.save()
        return instance

    def update(self, instance: AnimeModel, validated_data):
        if characters := validated_data.pop("characters"):
            for character in characters:
                character_instance = CharacterModel.objects.get(mal_id=character["mal_id"])
                instance.characters.add(character_instance)

        if genres := validated_data.pop("genres"):
            for genre in genres:
                genre_instance = AnimeGenreModel.objects.get(mal_id=genre["mal_id"])
                instance.genres.add(genre_instance)

        for attr, val in validated_data:
            setattr(instance, attr, val)

        instance.save()
        return instance
