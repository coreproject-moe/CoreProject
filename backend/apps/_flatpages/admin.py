from django.contrib import admin
from django.db import models
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget

# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
