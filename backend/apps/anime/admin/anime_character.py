from django.contrib import admin

from ..models import AnimeCharacterModel

# Register your models here.


@admin.register(AnimeCharacterModel)
class AnimeCharacterAdmin(admin.ModelAdmin):
    pass
