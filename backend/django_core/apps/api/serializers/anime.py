from apps.anime.models import AnimeModel, AnimeNameSynonymModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_theme import AnimeThemeModel
from rest_framework import serializers

from django.urls import reverse_lazy


class AnimeGETSerializer(serializers.ModelSerializer):
    name_synonyms = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )

    class Meta:
        model = AnimeModel
        exclude = (
            "genres",
            "themes",
            "characters",
            "studios",
            "producers",
            "staffs",
            "recommendations",
            "episodes",
        )

    def to_representation(self, instance: AnimeModel):
        ret = super().to_representation(instance)
        # Hyperlink
        ret["genres"] = reverse_lazy("anime-genres", args=[instance.pk])
        ret["themes"] = reverse_lazy("anime-themes", args=[instance.pk])
        ret["characters"] = reverse_lazy("anime-characters", args=[instance.pk])
        ret["studios"] = reverse_lazy("anime-studios", args=[instance.pk])
        ret["producers"] = reverse_lazy("anime-producers", args=[instance.pk])
        ret["staffs"] = reverse_lazy("anime-staffs", args=[instance.pk])
        ret["recommendations"] = reverse_lazy("anime-recommendations", args=[instance.pk])
        ret["episodes"] = reverse_lazy("anime-episodes", args=[instance.pk])
        return ret


class AnimePOSTSerializer(serializers.ModelSerializer):
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


class AnimeGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeGenreModel
        fields = "__all__"


class AnimeThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeThemeModel
        fields = "__all__"
