from ninja import Router

router = Router()


from .anime_character import router as anime_character_router
from .anime_genre import router as anime_genre_router
from .anime_info import router as anime_info_router
from .anime_producer import router as anime_producer_router
from .anime_studio import router as anime_studio_router
from .anime_theme import router as anime_theme_router

router.add_router("", anime_info_router, tags=["anime_info"])
router.add_router("", anime_genre_router, tags=["anime_info"])
router.add_router("", anime_producer_router, tags=["anime_info"])
router.add_router("", anime_studio_router, tags=["anime_info"])
router.add_router("", anime_character_router, tags=["anime_info"])
router.add_router("", anime_theme_router, tags=["anime_info"])


from .episode import router as episode_router
from .episode_timestamp import router as episode_timestamp_router
from .episode_comment import router as episode_comment_router

router.add_router("", episode_router, tags=["anime_episodes"])
router.add_router("", episode_timestamp_router, tags=["anime_episodes"])
router.add_router("", episode_comment_router, tags=["anime_episodes"])
