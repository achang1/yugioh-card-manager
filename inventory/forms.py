from django import forms
from django.contrib.auth.models import User
from django.core import validators


class SignUpForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=30, required=True, label='Enter username. Between 5-30 characters.')
    first_name = forms.CharField(max_length=30, required=True, label='Enter first name.')
    last_name = forms.CharField(max_length=30, required=True, label='Enter last name.')
    email = forms.EmailField(max_length=100, required=True, label='Enter email.')
    verify_email = forms.EmailField(max_length=100, required=True, label='Confirm email.')
    password = forms.EmailField(max_length=100, required=True, widget=forms.PasswordInput, label='Enter password.')
    verify_password = forms.EmailField(max_length=100, required=True, widget=forms.PasswordInput, label='Confirm password.')

    def clean_username(self):
        username = self.cleaned_data['username']
        res = User.objects.filter(username=username)
        
        if res.count():
            raise forms.ValidationError("Username already exists.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        verify_email = self.cleaned_data['verify_email'].lower()
        res = User.objects.filter(email=email)

        if email != verify_email:
            raise forms.ValidationError("Make sure emails match.")
        if res.count():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        verify_password = self.cleaned_data['verify_password']

        if password and verify_password and password != verify_password:
            raise forms.ValidationError("Make sure passwords match.")

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['first_name'],
            self.cleaned_data['last_name'],
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )
        return user

# class FormName(forms.ModelForm):
#     name = forms.CharField(max_length=100, unique=True)
#     description = forms.CharField(max_length=500)
#     attribute = forms.CharField(max_length=30)
#     type = forms.CharField(max_length=30)
#     rarity = forms.CharField(max_length=5)
#     colour = forms.CharField(max_length=30)

# class MonsterForm(forms.ModelForm):
#     class Meta:
