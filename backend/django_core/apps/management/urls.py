from . import views
from django.urls import path


urlpatterns = [
    path(
        "characters/", views.manage_characters_sync_call, name="manage_characters_sync_call"
    ),
    path(
        "characters/<int:id>/",
        views.manage_individual_characeters_sync_call,
        name="manage_individual_characeters_sync_call",
    ),
    path(
        "characters/<int:id>/log/   ",
        views.get_individual_character_sync_call_log,
        name="get_individual_character_sync_call_log",
    ),
]
