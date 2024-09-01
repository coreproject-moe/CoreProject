import strawberry_django
from strawberry import auto

from apps.episodes.models import EpisodeModel
from .comment import CommentType


@strawberry_django.type(EpisodeModel)
class EpisodeType:
    episode_number: auto
    episode_name: auto
    episode_thumbnail: auto

    episode_summary: auto
    episode_comments: list["CommentType"]
    episode_timestamps: auto

    episode_length: auto
    episode_type: auto

    # providers: dict[str, str]
