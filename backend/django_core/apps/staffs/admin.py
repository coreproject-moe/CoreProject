from django.contrib import admin

from .models import StaffAlternateNameModel, StaffModel

# Register your models here.


@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin[StaffModel]):
    pass


@admin.register(StaffAlternateNameModel)
class StaffAlternateNameAdmin(admin.ModelAdmin[StaffAlternateNameModel]):
    pass
