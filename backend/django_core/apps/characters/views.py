import json
from .tasks import call_command
from django.shortcuts import render
from .forms import CharacterManagementForm

from django.http import JsonResponse
from .models import CharacterLogModel


async def manage_characters(request):
    form = CharacterManagementForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            call_command(form.cleaned_data["reset"])

    return render(request, "characters/character_task.html", {"form": form})


async def get_individual_character_log(request, id):
    database = await CharacterLogModel.objects.aget(pk=id)
    return JsonResponse(
        {
            "logs": database.logs,
            "log_dictionary": database.log_dictionary,
        },
        safe=False,
    )


async def manage_individual_characeters(request, id: int):
    pass
