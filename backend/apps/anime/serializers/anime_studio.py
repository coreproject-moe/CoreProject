from rest_framework import serializers

from ..models import AnimeStudioModel, AnimeInfoModel


class AnimeStudioSerializer(serializers.ModelSerializer):
    mal_id = serializers.IntegerField()
    name = serializers.CharField()
    type = serializers.CharField()

    def create(self, validated_data):
        instance, created = AnimeStudioModel.objects.get_or_create(
            mal_id=validated_data["mal_id"],
            name=validated_data["name"],
            type=validated_data["type"],
        )

        AnimeInfoModel.objects.get(pk=self.context["anime_id"]).anime_studios.add(
            instance
        )

        return instance
