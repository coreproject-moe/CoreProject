from django import forms
from django.contrib.auth import get_user_model

from ..upload.models import AnimeInfoModel
from custom.forms.mixins.validate_password import ValidatePasswordMixin


class UserEditInfoForm(forms.ModelForm, ValidatePasswordMixin):
    confirm_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "input",
                "value": "",
                "placeholder": "Confirm Password",
                "autocomplete": "new-password",
            },
        ),
    )

    class Meta:
        model = get_user_model()

        fields = [
            "first_name",
            "last_name",
            "username",
            "password",
            "avatar",
            "email",
            "date_joined",
        ]

        widgets = {
            "avatar": forms.FileInput(
                attrs={
                    "class": "file-input is-clickable",
                    "placeholder": "Upload avatar",
                    "style": "z-index:1000000;",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "First Name",
                    "autocomplete": "off",
                },
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Last Name",
                    "autocomplete": "off",
                },
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Username",
                    "autocomplete": "off",
                },
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "input is-unselectable",
                    "style": "background-color:black; border:1px solid var(--border-color); color:white !important;",
                    "placeholder": "Email",
                    "readonly": True,
                    "disabled": True,
                },
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "input",
                    "value": "",
                    "placeholder": "Password",
                    "autocomplete": "new-password",
                },
            ),
            "date_joined": forms.DateInput(
                attrs={
                    "class": "input is-static is-unselectable",
                    "placeholder": "Date Joined",
                    "readonly": True,
                    "disabled": True,
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Disable requirement on `Password` and `Date Joined` field.
        self.fields["password"].required = False
        self.fields["date_joined"].required = False

        # Conditionally add this field
        if self.instance.avatar:
            self.fields["clear_image"] = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        self.validate_password(cleaned_data)

        # Remove dangerous fields
        cleaned_data.pop("email")

        # Delete the images if a user wishes to do so.
        if cleaned_data.get("clear_image"):
            self.instance.avatar.delete()

        return cleaned_data


class AnimeInfoEditForm(forms.ModelForm):
    class Meta:
        model = AnimeInfoModel
        fields = [
            "anime_name",
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
