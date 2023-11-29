from rest_framework import serializers


class AnimeCommentSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(read_only=True)
    user = serializers.CharField(read_only=True)
    text = serializers.CharField()
    path = serializers.CharField(required=False)
