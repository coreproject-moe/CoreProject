from rest_framework import serializers

from ..models import AnimeInfoModel


class AnimeInfoSerializer(serializers.ModelSerializer):
    # Everything is generic

    class Meta:
        model = AnimeInfoModel
        fields = "__all__"
