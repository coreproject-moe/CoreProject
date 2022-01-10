from django.shortcuts import render

# Create your views here.


async def home_page(request):
    return render(request, "home/index.html")
