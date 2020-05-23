from django import forms
from django.core import validators

def check_for_v(value):
    if value[0].lower() != 'v':
        raise forms.ValidationError("Name should start with v")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_v])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, 
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])