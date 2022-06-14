from rest_framework import serializers

from ..models import AnilistModel


class AnilistSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnilistModel
        fields = "__all__"
