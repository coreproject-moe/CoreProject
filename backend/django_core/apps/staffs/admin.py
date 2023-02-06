from django.contrib import admin

from .models import StaffModel

# Register your models here.


@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin[StaffModel]):
    pass
