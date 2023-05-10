from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from . import models

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name',
            'phone', 'email', 'description',
            'category', 'picture',
            )

    def clean(self): # Usado para fazer validações que depende de outros campos
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'sobrenome não pode ser igual ao nome',
                code='invalid',
                )
            self.add_error(
                'last_name', msg
            )

        return super().clean()


class RegisterForm(UserCreationForm):
    ...
    