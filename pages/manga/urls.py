from django.urls import path
from .views import *

urlpatterns = [
    path("", manga_home_page, name="manga_home_page"),
]
