from django.contrib import admin
from core.admin import site
from .models import AnimeStudioModel

# Register your models here.


class AnimeStudioAdmin(admin.ModelAdmin):
    search_fields = ["name"]


site.register(AnimeStudioModel, AnimeStudioAdmin)
