from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from ..models import AnimeInfoModel
from ..serializers import EpisodeCommentSerializer

# Create your views here.


class EpisodeCommentView(ModelViewSet):
    """
    Returns :
        - Comments
    """

    serializer_class = EpisodeCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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
            .episode_comments.all()
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
        serializer.save(user=self.request.user)
