from crispy_forms.helper import FormHelper

from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.conf import settings
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm["CustomUser"]):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm["CustomUser"]):
    class Meta:
        model = CustomUser
        fields = ("email",)


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username or Email",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False

        # https://stackoverflow.com/a/29717314
        for visible in self.visible_fields():
            # Add tailwind classes
            visible.field.widget.attrs[
                "class"
            ] = "input w-full text-white font-semibold max-w-xs border-[3px] border-warning focus:outline-0"
            visible.field.widget.attrs["style"] = "--tw-bg-opacity: 0.3"


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "autocomplete": "new-password",
            }
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "autocomplete": "new-password",
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False

        # https://stackoverflow.com/a/29717314
        for visible in self.visible_fields():
            # Add tailwind classes
            visible.field.widget.attrs[
                "class"
            ] = "input w-full text-white font-semibold max-w-xs border-[3px] border-warning focus:outline-0"
            visible.field.widget.attrs["style"] = "--tw-bg-opacity: 0.3"


class UsernameWithDiscriminatorForm(forms.Form):
    username = forms.CharField()
    discriminator = forms.IntegerField(
        max_value=int("9" * settings.DISCRIMINATOR_LENGTH),
        min_value=1,
    )
