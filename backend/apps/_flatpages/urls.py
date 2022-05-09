from django.urls import re_path
from django.contrib.flatpages import views

urlpatterns = [
    re_path(r"^(?P<url>.*/)$", views.flatpage),
]
