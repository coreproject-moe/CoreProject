import strawberry_django
from strawberry import auto
from apps.episodes.models import EpisodeModel
from .comment import CommentInput
import datetime


@strawberry_django.input(EpisodeModel)
class EpisodeInput:
    episode_number: auto
    episode_name: auto
    episode_thumbnail: auto

    episode_summary: auto
    # episode_comments: list["CommentInput"] | None = None
    # episode_timestamps: datetime.datetime

    episode_length: auto
    episode_type: auto

    # providers: auto
