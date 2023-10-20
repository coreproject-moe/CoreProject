from django.shortcuts import  render

from ...user.forms import LoginForm

def login_view(request):
    form = LoginForm()
    context = {
        "form": form
    }

    return render(request, "user/login.html", context)
