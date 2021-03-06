# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-20 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields
import yolo.models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='yolo',
            name='Image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='yolo/yolo/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='yolo',
            name='where',
            field=models.CharField(blank=True, help_text='Where? Write in the form of lng,lat (for example, 120.13456, 110, 314566', max_length=50, validators=[yolo.models.lnglat_validator]),
        ),
        migrations.AddField(
            model_name='yolo',
            name='category_set',
            field=models.ManyToManyField(blank=True, to='yolo.Category'),
        ),
    ]
