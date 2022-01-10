from django.shortcuts import render
from pages.faq.models import PageModel

# Create your views here.


def faq_page(request):
    post = PageModel.objects.first()
    return render(request, "faq/index.html", {"post": post})
