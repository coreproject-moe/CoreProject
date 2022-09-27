from django import forms


class CharacterManagementForm(forms.Form):
    reset = forms.BooleanField()
