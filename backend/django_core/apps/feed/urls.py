from django.urls import path
from . import views

urlpatterns = [
    path("anime/", views.all_anime_ids, name="all_anime_id_feed"),
]
