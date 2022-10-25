from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

from django import forms 
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.layout import Layout
from crispy_forms.helper import FormHelper

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)



class UserRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
               FloatingField("first_name"),
        )
    class Meta:
        model = CustomUser
        fields = "__all__"