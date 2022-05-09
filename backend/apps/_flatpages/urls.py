from django.contrib.flatpages import views
from django.urls import re_path

urlpatterns = [
    re_path(r"^(?P<url>.*/)$", views.flatpage),
]
