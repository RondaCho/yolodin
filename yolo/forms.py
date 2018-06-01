from django import forms
from .models import Yolo


class YoloForm(forms.ModelForm):
    class Meta:
        model = Yolo
        fields = '__all__'