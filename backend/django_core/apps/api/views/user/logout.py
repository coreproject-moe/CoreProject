from apps.api.models import Token
from ninja import Router

from django.http import HttpRequest, HttpResponse

from ...auth import AuthBearer

router = Router()


@router.delete("/logout", auth=AuthBearer())
def post_user_logout_info(request: HttpRequest) -> HttpResponse:
    token: Token = Token.objects.get(user=request.auth)
    token.delete()
    return HttpResponse("Successful", status=200)
