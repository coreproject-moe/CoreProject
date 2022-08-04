from django.contrib import admin

from .models import AnilistModel, KitsuModel, MalModel

# Register your models here.

admin.site.register([AnilistModel, MalModel, KitsuModel])
