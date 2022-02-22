from .views import *
from django.urls import path

urlpatterns = [
    path("login/", login_page, name="login_page"),
    path("logout/", logout, name="logout_page"),
    path("register/", register_page, name="register_page"),
]
