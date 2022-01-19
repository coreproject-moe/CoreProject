"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    (path("admin/", admin.site.urls) if settings.DEBUG else None),
    # Pages
    path("home/", include("pages.home.urls")),
    path("authentication/", include("pages.authentication.urls")),
    path("user/", include("pages.users.urls")),
    path("anime/", include("pages.anime.urls")),
    path("manga/", include("pages.manga.urls")),
    path("ost/", include("pages.ost.urls")),
    path("shots/", include("pages.shots.urls")),
    # Api
    path("api/v1/avatar/", include("api.v1.avatar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Leave everything to react.
# https://stackoverflow.com/questions/40826295/react-routing-and-django-url-conflict
# re_path(r"^(?:.*)/?$", anime_home_page, name="anime_home_page"),