# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-09 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20160609_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
    ]
