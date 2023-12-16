from apps.anime.models import AnimeModel
from apps.comments.models import CommentModel
from apps.episodes.models import EpisodeModel
from django.http import HttpRequest
from rest_framework import generics, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ....serializers.comments import CommentSerializer

# If we need to revisit, take a look at our ChadGPT conversation
# https://chat.openai.com/share/06777217-e9a9-4fb4-bcfc-28e9f59be6f8


class EpisodeCommentAPIView(generics.ListAPIView):
    # this is due to drf-spectacular
    queryset = CommentModel.objects.none()
    # Searilizers
    serializer_class = CommentSerializer
    # Permissions
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # Pagination
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = get_object_or_404(
            get_object_or_404(AnimeModel, pk=self.kwargs["pk"]).episodes,
            episode_number=self.kwargs["episode_number"],
        ).episode_comments.all()
        return queryset

    def post(self, request: HttpRequest, pk: int, episode_number: int) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        episode_instance: EpisodeModel = AnimeModel.objects.get(pk=pk).episodes.get(
            episode_number=episode_number
        )

        # Serializer Data
        serializer_data = {
            "user": request.user,
            "text": serializer.validated_data["text"],
        }

        if path := serializer.validated_data.get("path"):
            episode_comment_model_instance = CommentModel.objects.get(path__match=path)
            episode_comment_instance = CommentModel.objects.create_child(
                parent=episode_comment_model_instance, **serializer_data
            )

        else:
            episode_comment_instance = CommentModel.objects.create_child(**serializer_data)

        episode_instance.episode_comments.add(episode_comment_instance)
        comment_serialier = self.get_serializer(episode_comment_instance)

        return Response(status=200, data=comment_serialier.data)
