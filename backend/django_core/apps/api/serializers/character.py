from apps.characters.models import CharacterModel
from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterModel
        fields = "__all__"
