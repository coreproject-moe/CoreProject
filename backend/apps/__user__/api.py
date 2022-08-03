from ninja.security import HttpBearer
from ninja import NinjaAPI

api = NinjaAPI()


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


@api.get("/bearer", auth=AuthBearer())
def bearer(request):
    return {"token": request.auth}
