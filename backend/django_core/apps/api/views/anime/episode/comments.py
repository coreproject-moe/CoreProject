from apps.anime.models import AnimeModel
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from apps.episodes.models.episode_comment import EpisodeCommentModel
from ....serializers.episode.comment import EpisodeCommentGETSerializer


class EpisodeCommentAPIView(generics.ListCreateAPIView):
    queryset = EpisodeCommentModel.objects.all()
    serializer_class = EpisodeCommentGETSerializer
    # Permissions
    permission_classes = (IsAuthenticatedOrReadOnly,)
