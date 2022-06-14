from rest_framework import serializers

from .models import AnilistModel, KitsuModel, MalModel


class MalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MalModel
        fields = "__all__"


class KitsuSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitsuModel
        fields = "__all__"


class AnilistSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnilistModel
        fields = "__all__"
