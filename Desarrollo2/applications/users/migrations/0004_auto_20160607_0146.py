# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 01:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160605_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='califica',
            name='valor_Calificacion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lista_peliculas_vistas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 6, 7, 1, 46, 52, 645605)),
        ),
    ]
