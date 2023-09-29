from django.shortcuts import render

def anime_home_view(request):
    return render(request,'anime/home.html')