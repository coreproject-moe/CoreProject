from apps.__user__.models import KitsuModel
from django.shortcuts import get_object_or_404
from ninja import Router

from ..schemas import *

router = Router()


@router.get("/kitsu", response=KitsuSchema)
def get_kitsu_info(request):
    response = get_object_or_404(KitsuModel, user=request.user)
    return response
