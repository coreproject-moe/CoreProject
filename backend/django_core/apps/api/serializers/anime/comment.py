from rest_framework import serializers


class AnimeCommentPOSTSerializer(serializers.Serializer):
    text = serializers.CharField()
