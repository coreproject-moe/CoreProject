from django.contrib import admin
from core.admin import site
from ..models import AnimeSynonymModel

# Register your models here.


class AnimeSynonymAdmin(admin.ModelAdmin):
    search_fields = ["name"]


site.register(AnimeSynonymModel, AnimeSynonymAdmin)
