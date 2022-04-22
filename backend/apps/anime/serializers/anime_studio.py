from rest_framework import serializers

from ..models import AnimeStudioModel


class AnimeStudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeStudioModel
        fields = "__all__"
