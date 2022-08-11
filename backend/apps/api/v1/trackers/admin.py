from core.admin import site

from .models import AnilistModel, KitsuModel, MalModel

# Register your models here.

site.register([AnilistModel, MalModel, KitsuModel])
