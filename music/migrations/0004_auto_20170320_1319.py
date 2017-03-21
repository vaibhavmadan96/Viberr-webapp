# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 07:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0003_auto_20170319_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='song',
            name='file_type',
            field=models.FileField(upload_to=b''),
        ),
    ]
