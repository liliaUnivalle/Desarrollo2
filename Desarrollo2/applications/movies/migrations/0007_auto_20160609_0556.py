# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-09 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20160609_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
