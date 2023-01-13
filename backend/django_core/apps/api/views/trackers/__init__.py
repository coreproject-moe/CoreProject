from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from ninja import Router

from ...schemas.trackers import TrackerDeleteSchema, TrackerSchema

router = Router()


@router.post("", response=TrackerSchema)
@login_required
def update_user_tracker_info(request: HttpRequest, payload: TrackerSchema):
    pass


@router.delete("", response=TrackerDeleteSchema)
@login_required
def delete_user_tracker_info(request: HttpRequest, payload: TrackerDeleteSchema):
    pass
