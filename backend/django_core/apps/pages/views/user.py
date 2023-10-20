from django.http import HttpRequest
from django.shortcuts import render

from ..forms.user import LoginForm


def login_view(request: HttpRequest):
    form = LoginForm(request.POST or None)

    return render(request, "user/login.html", context={"form": form})
