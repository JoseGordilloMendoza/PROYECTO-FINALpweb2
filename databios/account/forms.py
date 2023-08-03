from django import forms
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
       model = CustomUser
       fields = ['username', 'email', 'telefono_celular', 'password']
       # forms.py

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields=['username','password']


