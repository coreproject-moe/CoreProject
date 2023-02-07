from django.urls import path

from . import views

urlpatterns = [
    path("avatar/<int:user_id>", views.avatar_view, name="avatar_view"),
    path("sign_up/", views.sign_up_view, name="sign_up_view"),
]
