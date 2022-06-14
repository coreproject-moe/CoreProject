from django.contrib import admin
from .models import AnilistModel, MalModel, KitsuModel

# Register your models here.
admin.site.register([AnilistModel, MalModel, KitsuModel])
