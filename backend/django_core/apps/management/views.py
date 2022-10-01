# Create your views here.
from apps.characters.tasks import call_character_management_command
from django.shortcuts import render
from .forms import CharacterManagementForm

from django.http import JsonResponse, HttpResponse, HttpRequest
from .models import CharacterLogModel


def manage_characters_sync_call(request: HttpRequest) -> HttpResponse:
    form = CharacterManagementForm(request.POST or None)
    models = CharacterLogModel.objects.all()

    if request.method == "POST":
        if form.is_valid():
            call_character_management_command(form.cleaned_data["reset"])

    return render(request, "management/character.html", {"form": form, "models": models})


async def manage_individual_characeters_sync_call(request, id: int):
    pass


async def get_individual_character_sync_call_log(request, id: int) -> JsonResponse:
    database = await CharacterLogModel.objects.aget(pk=id)
    return JsonResponse(
        {
            "logs": database.logs,
            "log_dictionary": database.log_dictionary,
        },
        safe=False,
    )
