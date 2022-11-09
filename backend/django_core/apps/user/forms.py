from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.urls import reverse
from .models import CustomUser

from django import forms
from crispy_forms.bootstrap import FormActions
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.layout import Layout, Submit, HTML, ButtonHolder
from crispy_forms.helper import FormHelper


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class UsernameDiscriminatorForm(forms.Form):
    username = forms.CharField()
    username_discriminator = forms.IntegerField()


class UserRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField("first_name", required=True),
            FloatingField("last_name"),
            FloatingField("email", required=True),
            FloatingField("username", required=True),
            FloatingField("username_discriminator", required=True),
            FormActions(
                ButtonHolder(
                    Submit("submit", "Submit", css_class="btn-warning"),
                    HTML(
                        f"""
                            or
                            <a class='text-white' href={reverse('login_view')}>Login</a>
                        """
                    ),
                    css_class="d-flex justify-content-center gap-2 align-items-center",
                )
            ),
        )

    class Meta:
        model = CustomUser
        fields = "__all__"
