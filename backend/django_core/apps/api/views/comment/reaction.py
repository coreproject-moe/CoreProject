from typing import Literal

from apps.comments.models import CommentModel
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ...serializers.comments import CommentSerializer
from ...serializers.comments.reaction import CommentReactionSerializer


class CommentReactionAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request: HttpRequest, pk: int) -> Response:
        reaction_serailizer = CommentReactionSerializer(data=request.data)
        comment_instance = get_object_or_404(CommentModel, pk=pk)

        if reaction_serailizer.is_valid(raise_exception=True):
            reaction: Literal["upvote"] | Literal[
                "downvote"
            ] = reaction_serailizer.validated_data["reaction"]

            if reaction == "upvote":
                comment_instance.downvotes.remove(request.user)
                comment_instance.upvotes.add(request.user)

            elif reaction == "downvote":
                comment_instance.upvotes.remove(request.user)
                comment_instance.downvotes.add(request.user)

            comment_instance.save()
            serializer = CommentSerializer(
                comment_instance,
                context={
                    "request": request,
                },
            )
            return Response(status=200, data=serializer.data)

    def delete(self, request: HttpRequest, pk: int) -> Response:
        comment_instance = get_object_or_404(CommentModel, pk=pk)
        comment_instance.upvotes.remove(request.user)
        comment_instance.downvotes.remove(request.user)
        comment_instance.save()
        serializer = CommentSerializer(
            comment_instance,
            context={
                "request": request,
            },
        )
        return Response(status=200, data=serializer.data)
