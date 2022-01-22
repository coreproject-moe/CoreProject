from django.urls import path

from .views import *

urlpatterns = [
    path("", anime_home_page, name="anime_home_page"),
    path(
        "<str:anime_name>/",
        anime_details_page,
        name="anime_name_and_episode_page",
    ),
    path(
        "<str:anime_name>/<int:anime_episode>",
        anime_name_and_episode_page,
        name="anime_name_and_episode_page",
    ),
]
