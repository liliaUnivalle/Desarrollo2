# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20160604_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]