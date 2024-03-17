from typing import TYPE_CHECKING

from django.shortcuts import render

if TYPE_CHECKING:
    from ..request import HtmxHttpRequest


def upload_view(request: "HtmxHttpRequest"):
    return render(request, "upload/index.html")
