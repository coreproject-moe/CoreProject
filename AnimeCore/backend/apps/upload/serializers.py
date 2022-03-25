from rest_framework import serializers

from .models import AnimeInfoModel, EpisodeCommentModel, EpisodeModel


class EpisodeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeCommentModel
        exclude = ("id",)


class EpisodeSerializer(serializers.ModelSerializer):
    episode_comments = EpisodeCommentSerializer(many=True)

    class Meta:
        model = EpisodeModel
        exclude = ("id",)


class AnimeInfoSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, required=False)

    class Meta:
        model = AnimeInfoModel
        fields = "__all__"

    def create(self, validated_data):
        """
        {
            "episodes": [],
            "mal_id": 91328,
            "anime_name": "Gintama",
            "anime_name_japanese": "dsadas",
            "anime_source": "dsaasd",
            "anime_aired_from": "2022-03-22T18:55:17.825914Z",
            "anime_aired_to": "2022-03-22T18:55:17.843866Z",
            "anime_cover": null,
            "updated": "2022-03-21T20:24:48.661105Z"
        }
        """
        validated_data.pop("episodes", None)  # ignore

        data = AnimeInfoModel(**validated_data)
        data.save()

        return data
