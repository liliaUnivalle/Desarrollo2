# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-11 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_auto_20160611_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='nombre',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]
