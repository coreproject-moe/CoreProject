from django.urls import path

from .views import (
    get_individual_character_log,
    manage_characters,
    manage_individual_characeters,
)

urlpatterns = [
    path("management", manage_characters),
    path("management/<int:id>/", manage_individual_characeters),
    path("management/<int:id>/log", get_individual_character_log),
]
