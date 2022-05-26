from rest_framework import serializers

from ..models import AnimeInfoModel


class AnimeInfoSerializer(serializers.ModelSerializer):
    # Everything is generic
    anime_producers = serializers.HyperlinkedIdentityField(
        view_name="anime_producers-list", lookup_url_kwarg="anime_id"
    )

    class Meta:
        model = AnimeInfoModel
        fields = "__all__"
