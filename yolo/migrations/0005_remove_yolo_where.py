# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-15 08:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0004_auto_20180522_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yolo',
            name='where',
        ),
    ]
