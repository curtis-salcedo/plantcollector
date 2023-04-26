from django import forms
from django.forms import ModelForm, CheckboxInput
from .models import Watering

class WateringForm(ModelForm):
    class Meta:
        model = Watering
        fields = ['date', 'time', 'water']
        widgets = {
            'water': CheckboxInput(attrs={'class': 'filled-in'}),
        }
