from django.forms import EmailField, CharField, PasswordInput, Form, TextInput, IntegerField, NumberInput


class RegisterForm(Form):
    email = EmailField(widget=TextInput(attrs={
        'placeholder': 'Enter email'
    }))
    name = CharField(widget=TextInput(attrs={
        'placeholder': 'Enter first name'
    }))
    password = CharField(widget=PasswordInput(attrs={
        'placeholder': 'Enter password'
    }))


class MoneyForm(Form):
    money = IntegerField(widget=NumberInput(attrs={
        'placeholder': 'Enter sum',
        'min': 1,
        'max': 999999,
    }))
