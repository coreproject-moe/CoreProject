from django.urls import path
from .views import *


urlpatterns = [
    path("anime/<int:primary_key>/", anime_info_edit_page, name="anime_info_edit_page"),
]
