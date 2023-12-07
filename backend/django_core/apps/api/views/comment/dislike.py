from apps.comments.models import CommentModel
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class CommentDislikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @method_decorator(never_cache)
    def post(self, request: HttpRequest, pk: int) -> Response:
        comment_instance = get_object_or_404(CommentModel, pk=pk)
        comment_instance.dislikes.add(request.user)
        comment_instance.save()
        return Response(status=200)

    @method_decorator(never_cache)
    def delete(self, request: HttpRequest, pk: int) -> Response:
        comment_instance = get_object_or_404(CommentModel, pk=pk)
        comment_instance.dislikes.remove(request.user)
        comment_instance.save()
        return Response(status=200)
