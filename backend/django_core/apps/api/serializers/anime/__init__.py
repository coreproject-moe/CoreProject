from apps.anime.models import AnimeModel, AnimeNameSynonymModel
from rest_framework import serializers

from .genre import AnimeGenreSerializer
from .theme import AnimeThemeSerializer


class AnimeSerializer(serializers.ModelSerializer):
    genres = AnimeGenreSerializer(many=True, required=False)
    themes = AnimeThemeSerializer(many=True, required=False)
    name_synonyms = serializers.SlugRelatedField(
        many=True,
        slug_field="name",
        queryset=AnimeNameSynonymModel.objects.all(),
    )

    class Meta:
        model = AnimeModel
        fields = "__all__"
        read_only_fields = ["is_locked"]

    def update(self, instance: AnimeModel, validated_data) -> AnimeModel:
        name_synonyms = validated_data.pop("name_synonyms", [])

        for name in name_synonyms:
            _name, _ = AnimeNameSynonymModel.objects.get_or_create(name)
            instance.name_synonyms.add(_name)

        return instance

    def create(self, validated_data: dict[str, str | int]) -> AnimeModel:
        name_synonyms = validated_data.pop("name_synonyms", [])

        anime_model = AnimeModel.objects.create(**validated_data)

        for name_synonym in name_synonyms:
            _name, _ = AnimeNameSynonymModel.objects.get_or_create(name=name_synonym)
            anime_model.name_synonyms.add(_name)

        return anime_model
