from django.contrib import admin

from .models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin[Token]):
    autocomplete_fields = ["user"]
