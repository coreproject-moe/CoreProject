from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from django.contrib import admin

from .models import StaffModel

# Register your models here.


@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin[StaffModel], DynamicArrayMixin):
    pass
