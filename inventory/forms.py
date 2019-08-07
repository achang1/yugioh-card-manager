from django import forms
from django.core import validators

class UserForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, \
        validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        data = super().clean()
        email = data['email']
        verify_email = data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("Make sure emails match.")

class FormName(forms.Form):
    name = forms.CharField(max_length=100, unique=True)
    description = forms.CharField(max_length=500)
    attribute = forms.CharField(max_length=30)
    type = forms.CharField(max_length=30)
    rarity = forms.CharField(max_length=5)
    colour = forms.CharField(max_length=30)