from django.urls import reverse
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


from ..upload.models import AnimeInfoModel
from .forms import AnimeInfoEditForm

# Create your views here.


@staff_member_required
def anime_info_edit_page(
    request: HttpRequest,
    primary_key: int,
) -> HttpResponse:
    instance = AnimeInfoModel.objects.get(id=primary_key)
    form = AnimeInfoEditForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=instance,
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(
                reverse(
                    "anime_info_edit_page",
                    kwargs={
                        "primary_key": primary_key,
                    },
                )
            )

    return render(request, "edit/anime_info/index.html", {"form": form})
