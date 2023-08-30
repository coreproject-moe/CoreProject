from apps.anime.models import AnimeModel
from apps.episodes.models.episode_comment import EpisodeCommentModel
from django.http import HttpRequest
from django.utils.crypto import get_random_string
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response

from ....filters.comments import EpisodeCommentFilter
from ....serializers.episode.comment import EpisodeCommentSerializer

# If we need to revisit, take a look at our ChadGPT conversation
# https://chat.openai.com/share/06777217-e9a9-4fb4-bcfc-28e9f59be6f8


class EpisodeCommentAPIView(generics.ListAPIView):
    queryset = EpisodeCommentModel.objects.all()
    serializer_class = EpisodeCommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EpisodeCommentFilter
    # Permissions
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request: HttpRequest, pk: int, episode_number: int) -> Response:
        serializer: EpisodeCommentSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Serializer Data
        serializer_data = {
            "user": serializer.validated_data["user"],
            "text": serializer.validated_data["text"],
            "path": serializer.validated_data.get("path", get_random_string(4)),
        }

        episode_instance = AnimeModel.objects.get(pk=pk).episodes.get(
            episode_number=episode_number
        )
        episode_instance.episode_comments.add(
            EpisodeCommentModel.objects.create(**serializer_data)
        )

        return Response(status=200, data=serializer.data)
