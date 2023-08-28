from .views import AnimeAPIView, AnimeSpecificAPIView
from django.urls import path

urlpatterns = [
    path("anime/", AnimeAPIView.as_view()),
    path("anime/<int:pk>/", AnimeSpecificAPIView.as_view()),
]
