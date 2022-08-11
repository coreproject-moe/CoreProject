from django.contrib import admin
from .models import AnimeProducerModel
from core.admin import site

# Register your models here.


class AnimeProducerAdmin(admin.ModelAdmin):
    search_fields = ["name"]


site.register(AnimeProducerModel, AnimeProducerAdmin)
