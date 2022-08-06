from ninja import Router

router = Router()

from .kitsu import router as kitsu_router
from .mal import router as mal_router
from .anilist import router as anilist_router


router.add_router("", mal_router, tags=["trackers"])
router.add_router("", kitsu_router, tags=["trackers"])
router.add_router("", anilist_router, tags=["trackers"])
