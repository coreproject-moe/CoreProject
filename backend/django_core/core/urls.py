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
from django.views import debug
from django.views.generic import TemplateView
from .format import format_kokoro_color
from django.templatetags.static import static


handler400 = TemplateView.as_view(
    template_name="errors/base.html",
    extra_context={
        "svg": {
            "file": static("images/kaomoji/400.svg"),
            "width": 414,
            "height": 123,
        },
        "error_status_code": 400,
        "error_status": "bad request",
        "error_text": format_kokoro_color(
            "kokoro-chan faced some issues in trying to decipher that request."
            "In the meantime, you can try checking the URL and refreshing the page, "
            "or go back home, "
            "browse the forums or come say hi!"
        ),
    },
)
handler403 = TemplateView.as_view(
    template_name="errors/base.html",
    extra_context={
        "svg": {
            "file": static("images/kaomoji/403.svg"),
            "width": 321,
            "height": 118,
        },
        "error_status_code": 403,
        "error_status": "Forbidden",
        "error_text": format_kokoro_color(
            "Even to her precious user-kun, "
            "kokoro-chan has some secrets that she wants to hide. "
            "Well, since there's nothing you can do about that, "
            "you can go back home, browse the forums or come say hi! "
        ),
    },
)
handler404 = TemplateView.as_view(
    template_name="errors/base.html",
    extra_context={
        "svg": {
            "file": static("images/kaomoji/404.svg"),
            "width": 414,
            "height": 123,
        },
        "error_status_code": 404,
        "error_status": "Page Not Found",
        "error_text": format_kokoro_color(
            "Our hardworking kokoro-chan was unable to find that page. "
            "While she collects more data on it, "
            "why don't you go back home, "
            "explore some random anime, "
            "browse the forums or come say hi!"
        ),
    },
)
handler500 = TemplateView.as_view(
    template_name="errors/base.html",
    extra_context={
        "svg": {
            "file": static("images/kaomoji/500.svg"),
            "width": 387,
            "height": 114,
        },
        "error_status_code": 500,
        "error_status": "Internal Server Error",
        "error_text": format_kokoro_color(
            "Uh-oh, looks like our cute kokoro-chan worked really hard"
            "for the past few days and has now fallen asleep. "
            "You can wait for her to wake up by looking at the status page, "
            "or come say hi to other fellow kokoro-chan worshippers! "
            "ah- also let's wish her sweet dreams! "
        ),
    },
)

urlpatterns = [
    path("", debug.default_urlconf),
    #   Admin Site
    # ================
    path("admin/", admin.site.urls),
    #   Errors
    # ===========
    path("400/", handler400),
    path("403/", handler403),
    path("404/", handler404),
    path("500/", handler500),
    #   HTTP
    # =========
    path("user/", include("apps.user.urls")),
    #   OpenGraph
    # =============
    path("opengraph/", include("apps.opengraph.urls")),
    #   Api
    # ========
    path("api/", include("apps.api.urls")),
]
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path("__reload__/", include("django_browser_reload.urls")),
    ]
