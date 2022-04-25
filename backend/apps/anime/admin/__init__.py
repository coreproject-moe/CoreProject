# https://stackoverflow.com/questions/49293901/hide-model-from-main-admin-list-but-allow-creation-in-inline-editor
# def has_module_permission(self, request):
#     return False

from .anime_info import AnimeInfoAdmin
from .anime_genre import AnimeGenreAdmin
from .anime_studio import AnimeStudioAdmin
from .anime_synonym import AnimeSynonymAdmin
from .anime_producer import AnimeProducerAdmin
from .anime_character import AnimeCharacterAdmin

from .episode import EpisodeAdmin
from .episode_comment import EpisodeCommentAdmin
from .episode_timestamp import EpisodeTimestampAdmin
