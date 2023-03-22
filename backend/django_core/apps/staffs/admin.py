from django.contrib import admin

from .models import StaffAlternateNameModel, StaffModel

# Register your models here.


@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin[StaffModel]):
    search_fields = [
        "name",
        "given_name",
        "family_name",
        "alternate_names__name",
    ]


@admin.register(StaffAlternateNameModel)
class StaffAlternateNameAdmin(admin.ModelAdmin[StaffAlternateNameModel]):
    pass
