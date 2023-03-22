from django import forms
from django.conf import settings
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


class UsernameWithDiscriminatorForm(forms.Form):
    username = forms.CharField()
    discriminator = forms.IntegerField(
        max_value=int("9" * settings.DISCRIMINATOR_LENGTH),
        min_value=1,
    )
