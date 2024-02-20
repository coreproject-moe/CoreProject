from apps.anime.models import AnimeModel
from apps.comments.models import CommentModel
from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import generics, pagination, permissions
from rest_framework.response import Response
from rest_framework import status

from ...serializers.comments import CommentSerializer


class AnimeCommentAPIView(generics.ListAPIView):
    # this is due to drf-spectacular
    queryset = CommentModel.objects.none()

    # Permissions
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
    # Pagination
    pagination_class = pagination.LimitOffsetPagination
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

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

        anime_comment_instance = serializer.save()
        anime_instance.comments.add(anime_comment_instance)

        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
