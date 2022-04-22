from rest_framework import serializers

from ..models import AnimeThemeModel


class AnimeThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeThemeModel
        fields = "__all__"
