from django.urls import path

from .views import AnimeAPIView, AnimeGenresAPIView, AnimeSpecificAPIView

urlpatterns = [
    path("anime/", AnimeAPIView.as_view()),
    path("anime/genres/", AnimeGenresAPIView.as_view()),
    path("anime/<int:pk>/", AnimeSpecificAPIView.as_view()),
]
