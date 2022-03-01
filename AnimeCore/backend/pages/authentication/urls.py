from . import views
from django.urls import path

urlpatterns = [
    path("register/", views.RegisterPageView.as_view(), name="register_page"),
    path("login/", views.LoginPageView.as_view(), name="login_page"),
    path("logout/", views.logout, name="logout_page"),
]
