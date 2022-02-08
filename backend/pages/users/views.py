from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from custom.user.models import CustomUser

from .forms import UserEditInfoForm

# Create your views here.


@login_required()
def user_edit_info_page(request):
    instance = CustomUser.objects.get(id=request.user.id)
    form = UserEditInfoForm(request.POST or None, instance=instance)

    if request.method == "POST":
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect(reverse("user_edit_info_page"))

    return render(request, "user/edit_info/index.html", {"form": form})
