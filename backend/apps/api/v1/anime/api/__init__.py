from ninja import Router

router = Router()


from .anime_character import router as anime_character_router
from .anime_genre import router as anime_genre_router
from .anime_info import router as anime_info_router
from .anime_producer import router as anime_producer_router
from .anime_studio import router as anime_studio_router

router.add_router("", anime_info_router)
router.add_router("", anime_genre_router)
router.add_router("", anime_producer_router)
router.add_router("", anime_studio_router)
router.add_router("", anime_character_router)
