from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from user_agents import parse

# Create your views here.


def animecore(request: HttpRequest) -> HttpResponse:
    user_agent_parsed = parse(request.META["HTTP_USER_AGENT"])

    # user_agent_parsed.is_bot
    if True:
        return render(request, "frontend/bot_response.html")

    else:
        return render(request, "frontend/animecore.html")
