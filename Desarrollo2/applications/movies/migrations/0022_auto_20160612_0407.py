# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-12 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0021_auto_20160612_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('nombre', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='pelicula',
            name='tipos',
            field=models.ManyToManyField(to='movies.Tipo'),
        ),
    ]
