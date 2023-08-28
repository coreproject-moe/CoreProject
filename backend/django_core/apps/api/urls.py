from django.urls import path

from .views.anime import (
    AnimeAPIView,
    AnimeSpecificAPIView,
    AnimeSpecificGenreAPIView,
    AnimeSpecificThemeAPIView,
)
from .views.anime.genre import AnimeGenresAPIView, AnimeGenresSpecificAPIView
from .views.anime.theme import AnimeThemesAPIView, AnimeThemesSpecificAPIView

urlpatterns = [
    path("anime/", AnimeAPIView.as_view()),
    path("anime/<int:pk>/", AnimeSpecificAPIView.as_view()),
    path("anime/<int:pk>/genres/", AnimeSpecificGenreAPIView.as_view()),
    path("anime/<int:pk>/themes/", AnimeSpecificThemeAPIView.as_view()),
    path("anime/genres/", AnimeGenresAPIView.as_view()),
    path("anime/genres/<int:pk>/", AnimeGenresSpecificAPIView.as_view()),
    path("anime/themes/", AnimeThemesAPIView.as_view()),
    path("anime/themes/<int:pk>/", AnimeThemesSpecificAPIView.as_view()),
]
