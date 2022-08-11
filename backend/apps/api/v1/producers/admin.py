from django.contrib import admin
from .models import AnimeProducerModel

# Register your models here.


@admin.register(AnimeProducerModel)
class AnimeProducerAdmin(admin.ModelAdmin):
    search_fields = ["name"]
