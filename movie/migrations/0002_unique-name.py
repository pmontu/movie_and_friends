# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-04 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_movie-and-rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
