from rest_framework import serializers


class UsernameValiditySerializer(serializers.Serializer):
    username = serializers.CharField()
