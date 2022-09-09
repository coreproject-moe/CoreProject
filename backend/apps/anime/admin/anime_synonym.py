from django.contrib import admin

from ..models import AnimeSynonymModel

# Register your models here.


@admin.register(AnimeSynonymModel)
class AnimeSynonymAdmin(admin.ModelAdmin):
    search_fields = ["name"]
