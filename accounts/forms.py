from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from core.forms import BootstrapFormMixin


class LoginForm (BootstrapFormMixin, AuthenticationForm):
    pass


class RegistrationForm (BootstrapFormMixin, forms.ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords do not match.")

        return cd['password2']
        





