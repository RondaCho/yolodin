from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Din


class DinForm(forms.ModelForm):
    class Meta:
        model = Din
        fields = ['range', 'where', 'when', 'why', 'note']

        widgets = {
            'when' : SelectDateWidget,
        }