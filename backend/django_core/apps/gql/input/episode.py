from apps.episodes.models import EpisodeModel
from strawberry import auto
import strawberry_django


@strawberry_django.input(EpisodeModel)
class EpisodeInput:
    episode_number: auto
    episode_name: auto
    episode_thumbnail: auto

    episode_summary: auto
    # episode_comments: list["CommentInput"] | None = None

    episode_length: auto
    episode_type: auto

    # providers: auto
