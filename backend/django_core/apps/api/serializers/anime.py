from apps.anime.models import AnimeModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_theme import AnimeThemeModel
from rest_framework import serializers

from django.urls import reverse_lazy


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeModel
        fields = "__all__"
        extra_kwargs = {
            "banner_background_color": {
                "read_only": True,
            },
            "cover_background_color": {
                "read_only": True,
            },
        }

    def to_representation(self, instance: AnimeModel):
        ret = super().to_representation(instance)
        # Hyperlink
        ret["genres"] = reverse_lazy("anime-genres", args=[instance.pk])
        ret["themes"] = reverse_lazy("anime-themes", args=[instance.pk])
        ret["characters"] = reverse_lazy("anime-characters", args=[instance.pk])
        ret["studios"] = reverse_lazy("anime-studios", args=[instance.pk])
        ret["producers"] = reverse_lazy("anime-producers", args=[instance.pk])
        return ret


class AnimeGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeGenreModel
        fields = "__all__"


class AnimeThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeThemeModel
        fields = "__all__"
