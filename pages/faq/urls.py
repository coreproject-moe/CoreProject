from .views import *
from django.urls import path

urlpatterns = [
    path("", faq_page, name="faq_page"),
]
