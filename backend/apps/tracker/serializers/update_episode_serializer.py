from rest_framework import serializers


class UpdateEpisodeSerializer(serializers.Serializer):
    anime_id = serializers.IntegerField()
    episode_number = serializers.IntegerField()
