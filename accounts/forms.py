from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from core.forms import BootstrapFormMixin


class LoginForm (BootstrapFormMixin, AuthenticationForm):
    pass











