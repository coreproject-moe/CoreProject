from crispy_forms.helper import FormHelper

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

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
                "class": "input w-full text-white font-semibold max-w-xs border-[3px] border-warning focus:outline-0",
                "style": "--tw-bg-opacity: 0.3",
                "placeholder": "Username or Email",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "input w-full text-white font-semibold max-w-xs border-[3px] border-warning focus:outline-0",
                "style": "--tw-bg-opacity: 0.3",
                "placeholder": "Password",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "input w-full text-white font-semibold max-w-xs border-[3px] border-warning focus:outline-0",
                "style": "--tw-bg-opacity: 0.3",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "input w-full text-white font-semibold max-w-xs border-[3px] border-warning focus:outline-0",
                "style": "--tw-bg-opacity: 0.3",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "input w-full text-white font-semibold max-w-xs border-[3px] border-warning focus:outline-0",
                "style": "--tw-bg-opacity: 0.3",
                "autocomplete": "new-password",
            }
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "input w-full text-white font-semibold max-w-xs border-[3px] border-warning focus:outline-0",
                "style": "--tw-bg-opacity: 0.3",
                "autocomplete": "new-password",
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
