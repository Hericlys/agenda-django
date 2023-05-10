from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
    first_name = forms.CharField(
        required=True,
    )

    last_name = forms.CharField(
        required=True,
    )

    email = forms.EmailField(
        required=True,
    )


    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2' 
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Esse e-mail já está em uso',
                    code='invalid',
                )
            )

        return email    