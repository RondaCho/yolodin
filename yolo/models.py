import re
from django.db import models
from django.forms import ValidationError

from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

from taggit.managers import TaggableManager

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*), ([+=]?\d+\.?\d*)$)', value):
        raise ValidationError('Invalid LngLat Type')


class Yolo(models.Model):
    Image = ProcessedImageField(blank=True, upload_to='yolo/yolo/%Y/%m/%d',
                                processors=[Thumbnail(400,400)],
                                format='JPEG',
                                options={'quality':70})

    tags = TaggableManager()

    what = models.CharField(max_length=100, help_text='What?')
    where = models.CharField(max_length = 50, blank=True, validators=[lnglat_validator],
                              help_text='Where? Write in the form of lng,lat (for example, 120.13456, 110, 314566')
    category_set = models.ManyToManyField('Category', blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.what


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name