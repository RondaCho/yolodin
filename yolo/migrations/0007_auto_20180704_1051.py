# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-04 01:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yolo', '0006_auto_20180618_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='yolo',
            name='what',
            field=models.CharField(help_text='What?', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='what',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yolo.Yolo'),
        ),
        migrations.AddField(
            model_name='post',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]