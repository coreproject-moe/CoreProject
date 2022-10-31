from django.urls import path

from . import views

urlpatterns = [
    path("avatar/<int:user_id>", views.avatar_view, name="avatar_view"),
    path("signup/", views.signup_view, name="signup_view"),
    path("login/", views.login_view, name="login_view"),
    path(
        "username_discriminator_validity/",
        views.username_discriminator_endpoint,
        name="username_discriminator_endpoint",
    ),
]
