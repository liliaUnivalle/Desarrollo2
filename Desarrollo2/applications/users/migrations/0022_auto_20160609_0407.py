# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-09 04:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20160609_0404'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Califica',
            new_name='Calificacion',
        ),
        migrations.AlterModelOptions(
            name='calificacion',
            options={'verbose_name': 'Calificacion', 'verbose_name_plural': 'Calificaciones'},
        ),
        migrations.AlterModelOptions(
            name='coleccion',
            options={'verbose_name': 'Coleccion', 'verbose_name_plural': 'Colecciones'},
        ),
        migrations.AlterModelOptions(
            name='lista_personal',
            options={'verbose_name': 'Lista_personal', 'verbose_name_plural': 'Listas_personales'},
        ),
    ]
