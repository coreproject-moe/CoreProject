from django.http import HttpRequest
from django.shortcuts import render
from django_htmx.http import retarget


def toast(request: HttpRequest, message: str):
    response = render(request, "components/toast.html", { "message": message })
    return retarget(response, "#toast")