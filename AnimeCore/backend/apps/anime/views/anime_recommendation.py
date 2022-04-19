from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
)

from ..models import AnimeRecommendationModel
from ..permissions import IsSuperUserOrReadOnly
from ..serializers import AnimeRecommendationSerializer


class AnimeRecommendationView(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet,
):
    """
    Returns :
        - Comments
    """

    serializer_class = AnimeRecommendationSerializer
    permission_classes = [IsSuperUserOrReadOnly]

    def get_queryset(self):
        queryset = AnimeRecommendationModel.objects.filter(
            anime=self.kwargs["anime_id"]
        )
        return queryset

    def get_serializer_context(self):
        # Thanks StackOverFlow
        # https://stackoverflow.com/questions/31038742/pass-request-context-to-serializer-from-viewset-in-django-rest-framework
        context = super().get_serializer_context()
        context.update(
            {"anime_id": self.kwargs["anime_id"]},
        )
        return context
