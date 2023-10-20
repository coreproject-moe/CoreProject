from django.shortcuts import redirect, render

def login_view(request):
	if request.user.is_authenticated:
		return redirect("anime_home_view")

	context = {}
	return render(request, "user/login.html")