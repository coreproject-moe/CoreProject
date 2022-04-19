from rest_framework import serializers

from ..models import (
    AnimeInfoModel,
    AnimeRecommendationModel,
)


class AnimeRecommendationEntrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    mal_id = serializers.IntegerField()
    anime_name = serializers.CharField(read_only=True)
    anime_cover = serializers.CharField(read_only=True)


class AnimeRecommendationSerializer(serializers.ModelSerializer):
    entry = AnimeRecommendationEntrySerializer(many=False)

    class Meta:
        model = AnimeRecommendationModel
        exclude = ("anime",)

    def create(self, validated_data):
        instance, _ = AnimeRecommendationModel.objects.get_or_create(
            entry=AnimeInfoModel.objects.get(mal_id=validated_data["entry"]["mal_id"]),
            anime=self.context["anime_id"],
            mal_url=validated_data["mal_url"],
        )
        return instance
