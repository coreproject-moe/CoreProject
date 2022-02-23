from .views import *
from django.urls import path

urlpatterns = [
    path("login/", LoginPageView.as_view(), name="login_page"),
    path("logout/", logout, name="logout_page"),
    path("register/", RegisterPageView.as_view(), name="register_page"),
]
