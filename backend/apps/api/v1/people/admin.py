from django.contrib import admin

from .models import PeopleModel

# Register your models here.

admin.site.register([PeopleModel])
