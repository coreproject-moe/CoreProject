from ..schemas import *
from django.shortcuts import get_object_or_404
from ninja import Router

from apps.__user__.models import MalModel

router = Router()


@router.get("/mal", response=MALSchema)
def get_mal_info(request):
    response = get_object_or_404(MalModel, user=request.user)
    return response
