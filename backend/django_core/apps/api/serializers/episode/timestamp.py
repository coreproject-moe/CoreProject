from rest_framework import serializers


class EpisodeTimpstampSerializer(serializers.Serializer):
    user = serializers.CharField(read_only=True)
    timestamp = serializers.IntegerField()
