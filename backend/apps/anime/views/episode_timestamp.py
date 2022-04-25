from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from ..models import AnimeInfoModel
from ..serializers import EpisodeTimestampSerializer

# Create your views here.


class EpisodeTimestampView(ModelViewSet):
    """
    Returns :
        - Timestamps
    """

    serializer_class = EpisodeTimestampSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "user__username"

    def get_queryset(self):
        instance = AnimeInfoModel.objects.all()
        queryset = (
            get_object_or_404(
                instance,
                pk=self.kwargs["anime_id"],
            )
            .anime_episodes.get(
                episode_number__in=self.kwargs["episodes_episode_number"]
            )
            .episode_timestamps.all()
        )
        return queryset

    def get_serializer_context(self):
        # Thanks StackOverFlow
        # https://stackoverflow.com/questions/31038742/pass-request-context-to-serializer-from-viewset-in-django-rest-framework
        context = super().get_serializer_context()
        context.update(
            {
                "anime_id": self.kwargs["anime_id"],
                "episode_number": self.kwargs["episodes_episode_number"],
            }
        )
        return context

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )
