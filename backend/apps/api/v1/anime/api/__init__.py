from ninja import Router

router = Router()


from .anime_genre import router as anime_genre_router
from .anime_info import router as anime_info_router

router.add_router("", anime_info_router)
router.add_router("", anime_genre_router)
