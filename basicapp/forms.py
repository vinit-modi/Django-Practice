from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_botcatcher(self):
        data = self.cleaned_data["botcatcher"]
        if len(data) > 0:
            raise forms.ValidationError("GOTCHA BOT")
        return data
    