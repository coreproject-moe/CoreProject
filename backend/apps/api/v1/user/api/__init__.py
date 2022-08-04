from ninja import Router

router = Router()


from .kitsu import router as kitsu_router
from .mal import router as mal_router
from .user_info import router as user_router

router.add_router("", kitsu_router)
router.add_router("", user_router)
router.add_router("", mal_router)
