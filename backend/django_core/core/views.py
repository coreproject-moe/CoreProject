from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.templatetags.static import static

from .utilities.format import format_kokoro_color

ERROR_DICT = {
    400: {
        "svg": {
            "file": static("images/kaomoji/400.svg"),
            "width": 414,
            "height": 123,
        },
        "error_status": "bad request",
        "error_text": format_kokoro_color(
            "kokoro-chan faced some issues in trying to decipher that request."
            "In the meantime, you can try checking the URL and refreshing the page, "
            "or go back home, browse the forums or come say hi!"
        ),
    },
    403: {
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
    404: {
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
    500: {
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
}


async def home_view(request: HttpRequest) -> HttpResponse:
    context = {
        "cards": {
            "django": {
                "type": "Web Framework",
                "description": "The web framework for perfectionists with deadlines.",
                "logo": static("images/logos/django.svg"),
            },
            "requests": {
                "type": "HTTP Request library",
                "description": "Requests is an elegant and simple HTTP library for Python, built for human beings.",
                "logo": static("images/logos/requests.png"),
            },
            "celery": {
                "type": "Task Queue",
                "description": "Distributed Task Queue",
                "logo": static("images/logos/celery.svg"),
            },
        },
    }

    return render(request, "home/index.html", context)


async def four_zero_zero_view(
    request: HttpRequest,
    exception: None = None,
) -> HttpResponse:
    context = ERROR_DICT.get(400)
    context.setdefault("error_status_code", 400)
    return render(
        request,
        "errors/base.html",
        context,
    )


async def four_zero_three_view(
    request: HttpRequest, exception: None = None
) -> HttpResponse:
    context = ERROR_DICT.get(403)
    context.setdefault("error_status_code", 403)
    return render(
        request,
        "errors/base.html",
        context,
    )


async def four_zero_four_view(
    request: HttpRequest,
    exception: None = None,
) -> HttpResponse:
    context = ERROR_DICT.get(404)
    context.setdefault("error_status_code", 404)
    return render(
        request,
        "errors/base.html",
        context,
    )


async def five_zero_zero_view(request: HttpRequest) -> HttpResponse:
    context = ERROR_DICT.get(500)
    context.setdefault("error_status_code", 500)

    return render(
        request,
        "errors/base.html",
        context,
    )
