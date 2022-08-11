from django.contrib import admin

from .models import AnimeStudioModel

# Register your models here.


@admin.register(AnimeStudioModel)
class AnimeStudioAdmin(admin.ModelAdmin):
    search_fields = ["name"]
