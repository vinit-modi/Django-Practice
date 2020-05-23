from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    

    def clean(self):
        clean_all_data = super().clean()
        email = clean_all_data['email']
        verify_email = clean_all_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("Please make sure entered emails are match")