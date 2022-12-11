from ninja.security import APIKeyHeader

from django.http import HttpRequest


class AuthBearer(APIKeyHeader):
    param_name = "X-Token"

    def authenticate(self, request: HttpRequest, key: str) -> str:
        if key == "supersecret":
            return key
