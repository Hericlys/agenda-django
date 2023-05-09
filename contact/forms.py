from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'veio do novo campo',
            }   
        ),
        label='Primeiro nome',
        help_text='Texto de ajuda para o usuario'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    #   self.fields['first_name'].widget.attrs.update({
    #        'placeholder': 'First Name',
    #   })

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name',
            'phone', 'email', 'description',
            'category',
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

    def clean_first_name(self): # usado para validações expecificas de um campo
        first_name = self.cleaned_data.get('first_name')
        #if first_name == "ABC":
        #    raise ValidationError(
        #       'Não digite abc nesse campo'
        #    )
        return first_name