from django.contrib import admin

from .models import ProducerModel

# Register your models here.


@admin.register(ProducerModel)
class ProducerAdmin(admin.ModelAdmin[ProducerModel]):
    search_fields = ["name"]
