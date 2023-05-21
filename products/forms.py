from .models import Order
from django.forms import ModelForm, TextInput, DateInput, SelectDateWidget


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['date', 'city']
        widgets = {
            'date': DateInput(attrs={
                'placeholder': 'Enter date of delivery',
                'type': 'date'
            }),
            'city': TextInput(attrs={
                'placeholder': 'Enter city'
            }),
        }
