from django.urls import path

from . import views

urlpatterns = [
    path("avatar/<int:user_id>", views.avatar_view, name="avatar_view"),
    path("signup/", views.signup_view, name="signup_view"),
]
