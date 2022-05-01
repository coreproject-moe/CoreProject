from django.db.models import Avg
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import action
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
                "anime_id": self.kwargs.get("anime_id"),
                "episode_number": self.kwargs.get("episodes_episode_number"),
            }
        )
        return context

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )

    @action(detail=True)
    def total_watchtime(
        self,
        *args,
        **kwargs,
    ) -> Response:
        queryset = (
            AnimeInfoModel.objects.get(pk=kwargs["anime_id"])
            .anime_episodes.get(episode_number__in=kwargs["episode_number"])
            .episode_timestamps.all()
            .aggregate(Avg("timestamp"))
        )
        return Response(data=queryset)
