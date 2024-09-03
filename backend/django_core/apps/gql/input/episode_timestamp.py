from apps.episodes.models.episode_timestamp import EpisodeTimestampModel
from strawberry import auto
import strawberry_django


@strawberry_django.input(EpisodeTimestampModel)
class EpisodeTimestampInput:
    episode_pk: int
    timestamp: auto
