from django.urls import include, path

from .views import faq_page

urlpatterns = [
    path("faq/", faq_page, name="faq_page"),
]
