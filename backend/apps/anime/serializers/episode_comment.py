from rest_framework import serializers

from ..models import AnimeInfoModel, EpisodeCommentModel


class EpisodeCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = EpisodeCommentModel
        fields = "__all__"

    def create(self, validated_data):
        data = super().create(validated_data)

        AnimeInfoModel.objects.get(pk=self.context["anime_id"]).anime_episodes.get(
            episode_number=self.context["episode_number"]
        ).episode_comments.add(data)

        return data
