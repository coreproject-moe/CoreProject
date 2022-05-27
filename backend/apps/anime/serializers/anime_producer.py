from rest_framework_nested.relations import NestedHyperlinkedRelatedField

from ..models import AnimeProducerModel


class AnimeProducerSerializer(NestedHyperlinkedRelatedField):
    parent_lookup_kwargs = {"anime_id": "anime_id"}

    class Meta:
        model = AnimeProducerModel
        fields = "__all__"
        queryset = AnimeProducerModel.objects.all()
