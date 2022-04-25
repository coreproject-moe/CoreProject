from django.shortcuts import get_object_or_404

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from ..models import AnimeInfoModel
from ..serializers import EpisodeSerializer
from ..permissions import IsSuperUserOrReadOnly


class EpisodeView(
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    """
    Returns :
        - Detailed Episodes info
    """

    serializer_class = EpisodeSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    # https://stackoverflow.com/questions/61452449/how-to-change-lookup-field-in-model-viewset-to-other-unique-parameter-in-django
    lookup_field = "episode_number"

    def get_queryset(self):
        instance = AnimeInfoModel.objects.all()
        queryset = get_object_or_404(
            instance,
            pk=self.kwargs["anime_id"],
        ).anime_episodes.all()

        return queryset

    def get_serializer_context(self):
        # Thanks StackOverFlow
        # https://stackoverflow.com/questions/31038742/pass-request-context-to-serializer-from-viewset-in-django-rest-framework
        context = super().get_serializer_context()
        context.update(
            {"request": self.request},
        )
        return context
