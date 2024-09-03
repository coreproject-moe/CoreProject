from typing import cast

from apps.episodes.models import EpisodeModel
from apps.episodes.models.episode_timestamp import EpisodeTimestampModel
from apps.gql.functions.dictionary import clean_dictionary
from django.shortcuts import get_object_or_404
import strawberry
from strawberry import Info
import strawberry_django

from ..input.episode import EpisodeInput
from ..input.episode_timestamp import EpisodeTimestampInput
from ..permissions import IsAuthenticated, IsSuperUser
from ..types.episode import EpisodeType


@strawberry.type
class EpisodeMutation:
    @strawberry_django.mutation(
        permission_classes=[IsSuperUser],
        extensions=[strawberry_django.permissions.IsSuperuser()],
    )
    def add_episode(self, info: Info, data: EpisodeInput) -> EpisodeType:
        kwargs = {
            "episode_number": data.episode_number,
            "episode_name": data.episode_name,
            "episode_summary": data.episode_summary,
            "episode_length": data.episode_length,
            "episode_type": data.episode_type,
            # 'episode_timestamps': "",
            # "providers": data.providers,
        }
        model_data = clean_dictionary(dictionary=kwargs)

        instance = EpisodeModel.objects.create(**model_data)
        filtered_instance = instance.filter(episode_timestamps__user=info.context["user"])
        return cast(EpisodeType, filtered_instance)

    @strawberry_django.mutation(
        permission_classes=[IsAuthenticated],
        extensions=[strawberry_django.permissions.IsAuthenticated()],
    )
    def add_timestamp(self, info: Info, data: EpisodeTimestampInput) -> bool:
        kwargs = {
            "timestamp": data.timestamp,
            "user": info.context["user"],
        }

        episode_instance = get_object_or_404(EpisodeModel, pk=data.episode_pk)
        episode_timestamp_instance = EpisodeTimestampModel.objects.create(**kwargs)
        episode_instance.episode_timestamps.add(episode_timestamp_instance)

        return True

    def add_comments(self, info: Info, data: Info):
        pass
