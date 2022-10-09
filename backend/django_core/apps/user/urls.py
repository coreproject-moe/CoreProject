from . import views
from django.urls import path

urlpatterns = [
    path("avatar/<int:user_id>", views.avatar_view, name="avatar_view"),
]
