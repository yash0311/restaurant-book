# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-18 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20171117_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
