from apps.anime.models import AnimeModel
from apps.episodes.models.episode_timestamp import EpisodeTimestampModel
from django.http import HttpRequest
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from ....serializers.episode.timestamp import EpisodeTimpstampSerializer

# If we need to revisit, take a look at our ChadGPT conversation
# https://chat.openai.com/share/06777217-e9a9-4fb4-bcfc-28e9f59be6f8


class EpisodeTimeStampAPIView(generics.ListAPIView):
    serializer_class = EpisodeTimpstampSerializer
    filter_backends = (DjangoFilterBackend,)
    # Permissions
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self, *args, **kwargs):
        queryset = (
            AnimeModel.objects.get(pk=self.kwargs["pk"])
            .episodes.get(episode_number=self.kwargs["episode_number"])
            .episode_timestamps
        )
        return queryset

    def post(self, request: HttpRequest, pk: int, episode_number: int) -> Response:
        serializer: EpisodeTimpstampSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer_data = {
            "timestamp": serializer.validated_data["timestamp"],
            "user": request.user,
        }

        episode_instance = AnimeModel.objects.get(pk=pk).episodes.get(
            episode_number=episode_number
        )
        episode_instance.episode_timestamps.add(
            EpisodeTimestampModel.objects.create(**serializer_data)
        )

        return Response(status=200, data=serializer.data)
