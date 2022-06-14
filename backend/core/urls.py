"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/

"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

handler400 = TemplateView.as_view(template_name="400.html")
handler403 = TemplateView.as_view(template_name="403.html")
handler404 = TemplateView.as_view(template_name="404.html")
handler500 = TemplateView.as_view(template_name="500.html")

urlpatterns = [
    #   Admin
    # ==========
    path("admin/", admin.site.urls),
    #   ckEditor
    # ==============
    path("ckeditor/", include("ckeditor_uploader.urls")),
    #   Errors
    # ===========
    path("400/", handler400),
    path("403/", handler403),
    path("404/", handler404),
    path("500/", handler500),
    #   OpenAPI
    # ============
    path(
        "openapi",
        get_schema_view(
            title="CoreProject", description="API for all things …", version="1.0.0"
        ),
        name="openapi-schema",
    ),
    #   Api
    # ========
    path("api/v1/", include("apps.anime.apis")),
    path("api/v1/user/", include("apps.__user__.apis")),
    path("api/v1/tracker/", include("apps.tracker.apis")),
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/v1/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"
    ),
    #   Flatpages
    # ===============
    path("", include("apps.__flatpages__.urls")),
]

if settings.DEBUG:
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)


# from django.urls import get_resolver
# from pprint import pprint

# pprint(get_resolver().reverse_dict.keys())
