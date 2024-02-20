from apps.anime.models import AnimeModel
from apps.comments.models import CommentModel
from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import generics, pagination, permissions
from rest_framework.response import Response

from ...serializers.anime.comment import AnimeCommentPOSTSerializer
from ...serializers.comments import CommentSerializer


class AnimeCommentAPIView(generics.ListAPIView):
    # this is due to drf-spectacular
    queryset = CommentModel.objects.none()

    serializer_class = CommentSerializer
    # Permissions
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
    # Pagination
    pagination_class = pagination.LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentSerializer
        elif self.request.method == "POST":
            return AnimeCommentPOSTSerializer

    def get_queryset(self):
        queryset = (
            get_object_or_404(AnimeModel, pk=self.kwargs["pk"])
            .comments.all()
            .annotate(
                _ratio=Count("upvotes") - Count("downvotes"),
            )
            .order_by("-_ratio", "-created_at")
        )
        return queryset

    def post(self, request: HttpRequest, pk: int) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        anime_instance = AnimeModel.objects.get(pk=pk)

        # Serializer Data
        serializer_data = {
            "user": request.user,
            "text": serializer.validated_data["text"],
        }

        anime_comment_instance = CommentModel.objects.create_child(**serializer_data)

        anime_instance.comments.add(anime_comment_instance)

        comment_serialier = self.get_serializer(anime_comment_instance)
        return Response(status=200, data=comment_serialier.data)
