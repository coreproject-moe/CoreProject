from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def anime_home_page(request) -> HttpResponse:
    return render(request,'anime/index.html')

def anime_name_and_episode_page(request, anime_name, anime_episode) -> HttpResponse:
    pass
