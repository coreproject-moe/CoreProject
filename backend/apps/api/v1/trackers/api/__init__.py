from ninja import Router
from django.http import HttpRequest

from ..schemas import TrackerSchema, TrackerDeleteSchema

router = Router(tags=["trackers"])


@router.post("", response=TrackerSchema)
def update_user_tracker_info(request: HttpRequest, payload: TrackerSchema):
    pass


@router.delete("", response=TrackerDeleteSchema)
def delete_user_tracker_info(request: HttpRequest, payload: TrackerDeleteSchema):
    pass


from .anilist import router as anilist_router
from .kitsu import router as kitsu_router
from .mal import router as mal_router

router.add_router("", mal_router, tags=["trackers"])
router.add_router("", kitsu_router, tags=["trackers"])
router.add_router("", anilist_router, tags=["trackers"])
