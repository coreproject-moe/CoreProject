"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/

"""

from django.urls import path
from django.urls import include
from django.contrib import admin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    #    Pages
    # ============
    path("edit/", include("pages.edit.urls")),
    path("upload/", include("pages.upload.urls")),
    #   Api
    # ========
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/v1/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"
    ),
    # Rest endpoints ( Note that theres an 'underscore' before every route )
    path("api/v1/user/", include("api.v1.user.urls")),
    path("api/v1/capture/", include("api.v1.capture.urls")),
]
