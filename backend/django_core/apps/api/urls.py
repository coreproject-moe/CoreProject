from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.anime import (
    AnimeSpecificAPIView,
    AnimeViewSet,
)
from .views.characters import CharacterViewSet, CharacterSpecificAPIView
from .views.anime.genre import AnimeGenresAPIView, AnimeGenresSpecificAPIView
from .views.anime.theme import AnimeThemesAPIView, AnimeThemesSpecificAPIView
from .views.user.login import LoginAPIView
from .views.user.logout import LogoutAPIView

base_router = DefaultRouter()
base_router.register(r"anime", AnimeViewSet, basename="anime")
base_router.register(r"character", CharacterViewSet, basename="character")

urlpatterns = [
    path("", include(base_router.urls)),
    # Anime specific routes
    path("anime/<int:pk>/", AnimeSpecificAPIView.as_view()),
    path("anime/genres/", AnimeGenresAPIView.as_view()),
    path("anime/genres/<int:pk>/", AnimeGenresSpecificAPIView.as_view()),
    path("anime/themes/", AnimeThemesAPIView.as_view()),
    path("anime/themes/<int:pk>/", AnimeThemesSpecificAPIView.as_view()),
    # User routes
    path("user/login/", LoginAPIView.as_view()),
    path("user/logout/", LogoutAPIView.as_view()),
    # Character specific routes
    path("character/<int:pk>/", CharacterSpecificAPIView.as_view()),
]
