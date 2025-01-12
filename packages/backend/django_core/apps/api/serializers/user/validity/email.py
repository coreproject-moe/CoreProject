from rest_framework import serializers


class EmailValiditySerializer(serializers.Serializer):
    email = serializers.CharField()
