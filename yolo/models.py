import re
from django.db import models
from django.urls import reverse
from django.forms import ValidationError

from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail



def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*), ([+=]?\d+\.?\d*)$)', value):
        raise ValidationError('Invalid LngLat Type')


class Yolo(models.Model):
    image = ProcessedImageField(blank=True, upload_to='yolo/yolo/%Y/%m/%d',
                                processors=[Thumbnail(400, 400)],
                                format='JPEG',
                                options={'quality': 70})

    tag_set = models.ManyToManyField('Tag', blank=True)

    what = models.CharField(max_length=100, help_text='What?')
    where = models.CharField(max_length = 50, blank=True, validators=[lnglat_validator],
                              help_text='Do you know the location for this yolo?')
    category_set = models.ManyToManyField('Category', blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.what

    def get_absolute_url(self):
        return reverse('yolo:yolo_detail', args=[self.id])


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
