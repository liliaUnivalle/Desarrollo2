# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-09 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleccion',
            name='id_genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='li', to='users.Genero'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='generos',
            field=models.ManyToManyField(to='users.Genero'),
        ),
    ]
