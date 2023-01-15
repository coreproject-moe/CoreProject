from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from .models import StaffModel

# Register your models here.


@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass
