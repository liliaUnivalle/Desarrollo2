# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-11 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_genero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genero',
            name='nombre',
        ),
    ]
