"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/

"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #   Admin
    # ==========
    path("admin/", admin.site.urls),
    #   ckEditor
    # ==============
    path("ckeditor/", include("ckeditor_uploader.urls")),
    #   Errors
    # ===========
    path("400/", TemplateView.as_view(template_name="400.html")),
    path("403/", TemplateView.as_view(template_name="403.html")),
    path("404/", TemplateView.as_view(template_name="404.html")),
    path("500/", TemplateView.as_view(template_name="500.html")),
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
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/v1/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"
    ),
    path("api/v1/user/", include("apps.user.apis")),
    path("api/v1/", include("apps.anime.apis")),
    #   Flatpages
    # ===============
    path("", include("apps._flatpages.urls")),
]

if settings.DEBUG:
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)


# from django.urls import get_resolver
# from pprint import pprint

# pprint(get_resolver().reverse_dict.keys())
