import re
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.forms import ValidationError
from yolo.models import Yolo


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*), ([+=]?\d+\.?\d*)', value):
        raise ValidationError('Invalid LngLat Type')


class Din(models.Model):
    RANGE_CHOICES = (
        ('o', 'Public'), # open
        ('c', 'Private'), # closed
    )
    what = models.ForeignKey(Yolo, on_delete=models.SET_NULL, null=True)
    who = models.ForeignKey(settings.AUTH_USER_MODEL)
    range = models.CharField(max_length=1, choices=RANGE_CHOICES, help_text='Do you want others to see that you want this goal to happen? Then choose Public')
    when = models.DateField(verbose_name='objective due date', blank=True)
    why = models.ForeignKey('Value', blank=True, verbose_name='Personal Values related to this Yolo List', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        unique_together = ('what', 'who')

    def get_absolute_url(self):
        return reverse('din:din_detail', kwargs={'id': self.what_id, 'slug': self.who})


class Log(models.Model):
    what = models.ForeignKey(Din)
    message = models.TextField(help_text='Write out WHY you want it, personal meanings related to this and so on.', verbose_name='Why?')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class Value(models.Model):
    name = models.CharField(max_length=30, unique=True)
    definition = models.CharField(max_length=200)

    def __str__(self):
        return self.name
