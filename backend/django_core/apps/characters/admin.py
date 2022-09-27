from django.contrib import admin

from .models import CharacterModel, CharacterLogModel

# Register your models here.

admin.site.register([CharacterModel, CharacterLogModel])
