# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-03 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('din', '0008_auto_20180629_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='type',
        ),
        migrations.AlterField(
            model_name='log',
            name='message',
            field=models.TextField(help_text='This is for your current thoughts, status and extra notes'),
        ),
    ]
