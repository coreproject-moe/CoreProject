from django.http import HttpRequest as DjangoHttpRequest
from apps.user.models import CustomUser
from django.contrib.auth.models import AnonymousUser


class HttpRequest(DjangoHttpRequest):
    auth: CustomUser | AnonymousUser
