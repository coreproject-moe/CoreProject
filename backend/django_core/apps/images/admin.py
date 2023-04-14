from .models import ImageWithBrightnessAndBackgroundColor, Image
from django.contrib import admin

# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageWithBrightnessAndBackgroundColor)
class ImageWithBrightnessAndBackgroundColorAdmin(admin.ModelAdmin):
    pass
