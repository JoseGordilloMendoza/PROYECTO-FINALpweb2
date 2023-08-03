from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
       model = CustomUser
       fields = ['username', 'email', 'telefono_celular', 'password']
