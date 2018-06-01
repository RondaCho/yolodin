from django import forms
from django.forms.widgets import SelectDateWidget
from .models import MyYolo


class MyYoloForm(forms.ModelForm):
    class Meta:
        model = MyYolo
        fields = ['what', 'range', 'where', 'when', 'why', 'note']

        widgets = {
            'when' : SelectDateWidget,
        }