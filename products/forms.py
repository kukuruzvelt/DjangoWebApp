from .models import Order
from django.forms import ModelForm, TextInput, DateInput
import datetime


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['date', 'city']
        widgets = {
            'date': DateInput(attrs={
                'placeholder': 'Enter date of delivery',
                'type': 'date',
                'min': datetime.date.today() + datetime.timedelta(days=1)
            }),
            'city': TextInput(attrs={
                'placeholder': 'Enter city'
            }),
        }
