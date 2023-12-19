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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf.urls.static import static
from . import views

# from django.views import debug


# Admin site Branding
admin.site.site_header = "CoreProject administration"
admin.site.site_title = "CoreProject site admin"

# Error handlers
handler400 = views.four_zero_zero_view
handler403 = views.four_zero_three_view
handler404 = views.four_zero_four_view
handler500 = views.five_zero_zero_view

# Write your urls here

urlpatterns = [
    # Default django welcome page
    # path("", debug.default_urlconf),
    #   Admin
    # ================
    path("admin/", admin.site.urls),
    #   Django Defender Admin
    # ============================
    path("admin/defender/", include("defender.urls")),
    #   HTTP
    # =========
    path("user/", include("apps.user.urls")),
    #   API
    # ========
    path("api/v2/", include("apps.api.urls")),
    # Swagger
    path("api/v2/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v2/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    #  Pages
    # =======
    path("", include("apps.pages.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path("__reload__/", include("django_browser_reload.urls")),
        #   Errors
        # ===========
        path("400/", handler400),
        path("403/", handler403),
        path("404/", handler404),
        path("500/", handler500),
    ]
    # Serve media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
