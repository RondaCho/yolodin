from django import forms
from .models import Yolo, Post
from .widgets import LocationWidget, TuiEditorWidget, PreviewClearableFileInput


class YoloForm(forms.ModelForm):
    class Meta:
        model = Yolo
        fields = '__all__'
        widgets = {
            'image': PreviewClearableFileInput,
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'latlng': LocationWidget,
            'content': TuiEditorWidget,
        }
