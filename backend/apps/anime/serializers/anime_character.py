from rest_framework import serializers

from ..models import AnimeCharacterModel, AnimeInfoModel


class AnimeCharacterSerializer(serializers.Serializer):
    mal_id = serializers.IntegerField()
    name = serializers.CharField()
    character_image = serializers.ImageField()

    def create(self, validated_data):
        instance, created = AnimeCharacterModel.objects.get_or_create(
            mal_id=validated_data["mal_id"],
            name=validated_data["name"],
            character_image=validated_data["character_image"],
        )

        AnimeInfoModel.objects.get(pk=self.context["anime_id"]).anime_characters.add(
            instance
        )

        return instance
