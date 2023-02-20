from django.urls import path

from . import views

urlpatterns = [
    path("avatar/<int:user_id>", views.avatar_view, name="avatar_view"),
    path("signup/", views.signup_view, name="signup_view"),
    path("login/", views.login_view, name="login_view"),
    path(
        "__username_validity_endpoint__/",
        views.username_and_discriminator_validity_checker_view,
        name="username_and_discriminator_validity_checker_view",
    ),
]
