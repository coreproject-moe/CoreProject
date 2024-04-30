from typing import cast
from django.shortcuts import get_object_or_404
from strawberry import UNSET
from strawberry.types import Info

from apps.anime.models import AnimeModel, AnimeNameSynonymModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_theme import AnimeThemeModel
from apps.characters.models import CharacterModel
from apps.producers.models import ProducerModel
from apps.staffs.models import StaffModel

from apps.episodes.models import EpisodeModel
from apps.comments.models import CommentModel
import strawberry
import strawberry_django

from ..types.comment import Comment

from ..input.comment import CommentInput

from ..permissions import IsAuthenticated


@strawberry.type
class CommentMutation:
    @strawberry_django.mutation(
        permission_classes=[IsAuthenticated],
        extensions=[strawberry_django.permissions.IsAuthenticated()],
    )
    def add_comments(self, info: Info, data: CommentInput) -> Comment:
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

        # THIS IS VERY FRAGILE CODE.
        if data.model_type == "anime":
            anime_instance = AnimeModel.objects.get(pk=data.model_pk)
            anime_instance.comments.add(comment_instance)
        elif data.model_type == "episode":
            episode_instance = EpisodeModel.objects.get(pk=data.model_pk)
            episode_instance.episode_comments.add(comment_instance)

        return cast(Comment, comment_instance)
