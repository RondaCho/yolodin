import re
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.forms import ValidationError

from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail



def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*), ([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Yolo(models.Model):
    what = models.CharField(max_length=100, help_text='What?', unique=True)
    image = ProcessedImageField(blank=True, upload_to='yolo/yolo/%Y/%m/%d',
                                processors=[Thumbnail(400, 400)],
                                format='JPEG',
                                options={'quality': 70})
    category_set = models.ManyToManyField('Category', blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.what

    def get_absolute_url(self):
        return reverse('yolo:yolo_detail', args=[self.id])


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    what = models.ForeignKey(Yolo)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    latlng = models.CharField(max_length=50, blank=True)
    content = models.TextField() #textarea
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('yolo:post_detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies')

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created_at',)

    def __str__(self):
        return self.text