from typing import cast

from apps.anime.models import AnimeModel
from apps.comments.models import CommentModel
from apps.episodes.models import EpisodeModel
from django.http import Http404
from django.shortcuts import get_object_or_404
import strawberry
from strawberry import UNSET, Info
import strawberry_django

from ..input.comment import CommentInput
from ..permissions import IsAuthenticated
from ..types.comment import CommentType


@strawberry.type
class CommentMutation:
    @strawberry_django.mutation(
        permission_classes=[IsAuthenticated],
        extensions=[strawberry_django.permissions.IsAuthenticated()],
    )
    def add_comments(self, info: Info, data: CommentInput) -> CommentType:
        serializer_data = {
            "user": info.context["user"],
            "text": data.text,
        }
        if path := data.path:
            anime_comment_model_instance = get_object_or_404(CommentModel, path__match=path)
            comment_instance: "CommentModel" = CommentModel.objects.create_child(
                parent=anime_comment_model_instance, **serializer_data
            )
        else:
            comment_instance: "CommentModel" = CommentModel.objects.create_child(
                **serializer_data
            )

        if data.model_type == "anime":
            anime_instance = AnimeModel.objects.get(pk=data.model_pk)
            anime_instance.comments.add(comment_instance)
        elif data.model_type == "episode":
            episode_instance = EpisodeModel.objects.get(pk=data.model_pk)
            episode_instance.episode_comments.add(comment_instance)
        elif data != UNSET:
            # Raise this only if user tries to input something that we dont support
            raise Http404

        return cast(CommentType, comment_instance)
