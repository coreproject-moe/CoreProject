from django.urls import path

from .views.anime import (
    AnimeAPIView,
    AnimeSpecificAPIView,
)
from .views.anime.genre import AnimeGenresAPIView, AnimeGenresSpecificAPIView
from .views.anime.theme import AnimeThemesAPIView, AnimeThemesSpecificAPIView
from .views.user.logout import LogoutAPIView

urlpatterns = [
    path("anime/", AnimeAPIView.as_view()),
    path("anime/<int:pk>/", AnimeSpecificAPIView.as_view()),
    path("anime/genres/", AnimeGenresAPIView.as_view()),
    path("anime/genres/<int:pk>/", AnimeGenresSpecificAPIView.as_view()),
    path("anime/themes/", AnimeThemesAPIView.as_view()),
    path("anime/themes/<int:pk>/", AnimeThemesSpecificAPIView.as_view()),
    # User routes
    path("user/logout/", LogoutAPIView.as_view()),
]
