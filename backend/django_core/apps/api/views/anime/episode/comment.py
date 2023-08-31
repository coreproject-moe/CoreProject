from apps.anime.models import AnimeModel
from apps.episodes.models.episode_comment import EpisodeCommentModel
from django.http import HttpRequest
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from ....filters.comments import EpisodeCommentFilter
from ....serializers.episode.comment import EpisodeCommentSerializer

# If we need to revisit, take a look at our ChadGPT conversation
# https://chat.openai.com/share/06777217-e9a9-4fb4-bcfc-28e9f59be6f8


class EpisodeCommentAPIView(generics.ListAPIView):
    # this is due to drf-spectacular
    queryset = EpisodeCommentModel.objects.none()

    serializer_class = EpisodeCommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EpisodeCommentFilter
    # Permissions
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # Pagination
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset = (
            AnimeModel.objects.get(pk=self.kwargs["pk"])
            .episodes.get(episode_number=self.kwargs["episode_number"])
            .episode_comments
        )
        return queryset

    def post(self, request: HttpRequest, pk: int, episode_number: int) -> Response:
        serializer: EpisodeCommentSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        episode_instance = AnimeModel.objects.get(pk=pk).episodes.get(
            episode_number=episode_number
        )

        # Serializer Data
        serializer_data = {
            "user": request.user,
            "text": serializer.validated_data["text"],
        }

        if path := serializer.validated_data.get("path"):
            episode_comment_model_instance = EpisodeCommentModel.objects.get(
                path__match=path
            )
            episode_comment_instance = EpisodeCommentModel.objects.create_child(
                parent=episode_comment_model_instance, **serializer_data
            )

        else:
            episode_comment_instance = EpisodeCommentModel.objects.create(**serializer_data)

        episode_instance.episode_comments.add(episode_comment_instance)

        return Response(status=200, data=serializer.data)
