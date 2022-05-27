from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from ..models import AnimeInfoModel
from ..permissions import IsSuperUserOrReadOnly
from ..serializers import AnimeProducerSerializer


class AnimeProducerView(ViewSet):
    """
    Returns :
        - Producers
    """

    serializer_class = AnimeProducerSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = AnimeInfoModel.objects.all()

    def list(self, request, anime_id=None):
        queryset = self.queryset.filter(mal_id=anime_id)
        serializer = AnimeProducerSerializer(queryset, many=True)
        return Response(serializer.data)
