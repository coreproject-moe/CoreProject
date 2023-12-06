from apps.comments.models import CommentModel
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class CommentLikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request: HttpRequest, pk: int) -> Response:
        comment_instance = get_object_or_404(CommentModel, pk=pk)
        comment_instance.likes.add(request.user)
        comment_instance.save()
        return Response(status=200)

    def delete(self, request: HttpRequest, pk: int) -> Response:
        comment_instance = get_object_or_404(CommentModel, pk=pk)
        comment_instance.likes.remove(request.user)
        comment_instance.save()
        return Response(status=200)
