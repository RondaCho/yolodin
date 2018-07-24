from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Din, Log
from .widgets import DatePickerWidget


class DinForm(forms.ModelForm):
    class Meta:
        model = Din
        fields = ['range', 'when', 'why']
        widgets = {
            'when': DatePickerWidget,
        }


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['message']