# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-09 05:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20160609_0552'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Generos',
            new_name='Genero',
        ),
    ]
