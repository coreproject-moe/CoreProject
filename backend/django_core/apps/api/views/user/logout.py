from apps.api.models import Token
from django.http import HttpRequest, HttpResponse
from ninja import Router

from ...auth import AuthBearer

router = Router()


@router.delete("/logout", auth=AuthBearer())
def post_user_logout_info(request: HttpRequest) -> HttpResponse:
    token: Token = Token.objects.get(user=request.auth)
    token.delete()
    return HttpResponse("Successful", status=200)
