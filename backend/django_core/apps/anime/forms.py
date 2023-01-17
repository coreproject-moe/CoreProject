from django_admin_hstore_widget.forms import HStoreFormField

from django import forms

from .models import AnimeModel


class AnimeAdminModelForm(forms.ModelForm):
    anime_theme_openings = HStoreFormField()
    anime_theme_endings = HStoreFormField()

    class Meta:
        model = AnimeModel
        fields = "__all__"
