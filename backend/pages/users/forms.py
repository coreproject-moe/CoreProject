from django import forms
from django.contrib.auth import get_user_model

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
    clear_image = forms.BooleanField(required=False)

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
            "password",
            "avatar",
        ]

        widgets = {
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
            "avatar": forms.FileInput(
                attrs={
                    "class": "file-input is-clickable",
                    "placeholder": "Upload avatar",
                    "style": "z-index:1000000;",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "input",
                    "value": "",
                    "placeholder": "Password",
                    "autocomplete": "new-password",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Disable Password field.
        self.fields["password"].required = False

    def clean(self):
        cleaned_data = super().clean()
        self.validate_password(cleaned_data)

        if cleaned_data.get("clear_image"):
            self.instance.avatar.delete()

        return cleaned_data
