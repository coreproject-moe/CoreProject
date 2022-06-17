from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from ..models import AnimeInfoModel, AnimeStudioModel


class AnimeStudioSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        "anime_id": "anime__id",
    }

    class Meta:
        model = AnimeStudioModel
        fields = ["url", "mal_id", "name", "type"]

    def create(self, validated_data):
        instance, created = AnimeStudioModel.objects.get_or_create(
            mal_id=validated_data["mal_id"],
            name=validated_data["name"],
            type=validated_data["type"],
        )

        AnimeInfoModel.objects.get(pk=self.context["anime_id"]).anime_studios.add(
            instance
        )

        return instance
