from rest_framework import serializers

from ..models import (
    AnimeInfoModel,
)


class AnimeRecommendationEntrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    mal_id = serializers.IntegerField()
    anime_name = serializers.CharField(read_only=True)
    anime_cover = serializers.CharField(read_only=True)


class AnimeRecommendationSerializer(serializers.ModelSerializer):
    entry = AnimeRecommendationEntrySerializer(many=False)
