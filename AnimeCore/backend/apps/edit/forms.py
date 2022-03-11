from django import forms

from ..upload.models import AnimeInfoModel


class AnimeInfoEditForm(forms.ModelForm):
    class Meta:
        model = AnimeInfoModel
        fields = [
            "anime_name",
            "anime_cover",
        ]

        widgets = {
            "anime_name": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Anime Name",
                },
            ),
        }


class AnimeEpisodeEditForm(forms.ModelForm):
    pass
