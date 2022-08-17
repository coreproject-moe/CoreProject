from django.contrib import admin
from .models import StaffModel, StaffAlternateNameModel

# Register your models here.

admin.site.register([StaffModel, StaffAlternateNameModel])
