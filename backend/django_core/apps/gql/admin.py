from django.contrib import admin

from .models import Token

# Register your models here.


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin[Token]):
    autocomplete_fields = ["user"]
