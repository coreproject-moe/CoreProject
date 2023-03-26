from django.urls import path
from . import views

urlpatterns = [
    path("anime/", views.all_anime_ids, name="all_anime_id_feed"),
    path("character/", views.all_character_ids, name="all_character_id_feed"),
    path("producer/", views.all_producer_ids, name="all_producer_id_feed"),
    path("staff/", views.all_staff_ids, name="all_staff_id_feed"),
]
