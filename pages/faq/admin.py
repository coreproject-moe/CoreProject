from django.contrib import admin
from django.http.request import HttpRequest
from .models import PageModel

# Register your models here.
class PageModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        # Allow only one page
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(PageModel, PageModelAdmin)
