from .views import *
from django.urls import path


urlpatterns = [
    path("management", manage_characters),
    path("management/<int:id>/", manage_individual_characeters),
    path("management/<int:id>/log", get_individual_character_log),
]
