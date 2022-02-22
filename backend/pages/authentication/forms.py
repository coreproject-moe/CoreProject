from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class LoginForm(forms.Form):
    username = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "input ",
                "placeholder": "Username",
            }
        ),
    )

    password = forms.CharField(
        label="",
        min_length=8,
        max_length=1024,
        widget=forms.PasswordInput(
            attrs={
                "class": "input ",
                "placeholder": "Password",
            }
        ),
    )


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "input ",
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
            "email": forms.EmailInput(
                attrs={
                    "class": "input",
                    "placeholder": "Email",
                    "autocomplete": "off",
                },
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "input ",
                    "value": "",
                    "placeholder": "Password",
                    "autocomplete": "new-password",
                }
            ),
        }

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error(
                "confirm_password",
                """'Password' and 'Confirm Password' does not match.""",
            )

        if not password and not confirm_password:
            cleaned_data.pop("password")
            cleaned_data.pop("confirm_password")

        else:
            hashed_password = make_password(password)
            cleaned_data["password"] = hashed_password
            cleaned_data["confirm_password"] = hashed_password

        return cleaned_data
