from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from .models import FAQModel

# Create your views here.


def faq_page(request: HttpRequest) -> HttpResponse:
    model = FAQModel.objects.first()
    return render(
        request,
        "faq/index.html",
        {
            "content": model.content,
        },
    )
