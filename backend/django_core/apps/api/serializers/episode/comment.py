from rest_framework import serializers


class EpisodeCommentSerializer(serializers.Serializer):
    user = serializers.CharField(read_only=True)
    text = serializers.CharField()
    path = serializers.CharField(required=False)
