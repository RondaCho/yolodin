import re
from django.db import models
from django.forms import ValidationError

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*), ([+=]?\d+\.?\d*)$)', value):
        raise ValidationError('Invalid LngLat Type')


class Yolo(models.Model):
    what = models.CharField(max_length=100, help_text='What?')
    where = models.CharField(max_length = 50, blank=True, validators=[lnglat_validator],
                              help_text='Where?')
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.what

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name