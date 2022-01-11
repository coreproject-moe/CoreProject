from django.urls import path

from .views import *

urlpatterns = [
    path("/<str:anime_name>/<int:anime_episode>", anime_page, name="anime_page")
]
