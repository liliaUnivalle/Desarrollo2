# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 16:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160607_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista_peliculas_vistas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 6, 7, 16, 12, 26, 198378)),
        ),
    ]
