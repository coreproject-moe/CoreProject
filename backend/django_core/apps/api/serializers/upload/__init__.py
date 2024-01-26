from rest_framework import serializers


class ProviderSerializer(serializers.Serializer):
    api_key = serializers.CharField()
