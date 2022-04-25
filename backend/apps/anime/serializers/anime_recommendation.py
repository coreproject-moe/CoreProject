from rest_framework import serializers


class AnimeRecommendationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    mal_id = serializers.IntegerField()
    anime_name = serializers.CharField()
    anime_cover = serializers.CharField()
