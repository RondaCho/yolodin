# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-18 03:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0005_remove_yolo_where'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
