from django.contrib import admin

from .models import CharacterLogModel, CharacterModel

# Register your models here.

admin.site.register([CharacterModel, CharacterLogModel])
