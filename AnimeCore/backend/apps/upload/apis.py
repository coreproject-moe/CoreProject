from django.urls import path

from .views import AnimeInfoView

urlpatterns = [
    path("anime/", AnimeInfoView.as_view(), name="anime_info"),
]
