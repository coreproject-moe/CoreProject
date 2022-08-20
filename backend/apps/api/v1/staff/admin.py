from django.contrib import admin

from .models import StaffAlternateNameModel, StaffModel

# Register your models here.

admin.site.register([StaffModel, StaffAlternateNameModel])
