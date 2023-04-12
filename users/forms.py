from .models import User
from django.forms import ModelForm, TextInput, PasswordInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password', 'name']
        widgets = {
            'login': TextInput(attrs={
                'placeholder': 'Enter login'
            }),
            'password': PasswordInput(attrs={
                 'placeholder': 'Enter password'
            }),
            'name': TextInput(attrs={
                'placeholder': 'Enter name'
            }),
        }
