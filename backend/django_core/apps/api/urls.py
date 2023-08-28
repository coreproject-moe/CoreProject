from django.urls import path

from .views import AnimeAPIView, AnimeSpecificAPIView

urlpatterns = [
    path("anime/", AnimeAPIView.as_view()),
    path("anime/<int:pk>/", AnimeSpecificAPIView.as_view()),
]
