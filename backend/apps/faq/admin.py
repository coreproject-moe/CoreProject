from atexit import register

from django.contrib import admin

from .models import FAQModel

# Register your models here.


@admin.register(FAQModel)
class FAQAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True
