from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from ..models import AnimeProducerModel


class AnimeProducerSerializer(NestedHyperlinkedRelatedField):
    class Meta:
        model = AnimeProducerModel
        fields = "__all__"


