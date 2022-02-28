from django.urls import path
from .views import *


urlpatterns = [
    path("user_info/", user_info_edit_page, name="user_info_edit_page"),
    path("anime/<int:primary_key>/", anime_info_edit_page, name="anime_info_edit_page"),
]
