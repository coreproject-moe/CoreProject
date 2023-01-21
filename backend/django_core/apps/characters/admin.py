from django.contrib import admin

from .models import CharacterModel

# Register your models here.


@admin.register(CharacterModel)
class CharacterAdmin(admin.ModelAdmin[CharacterModel]):
    pass
