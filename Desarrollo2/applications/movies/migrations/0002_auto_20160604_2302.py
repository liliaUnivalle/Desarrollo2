# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-04 23:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='actores',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='actores',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='auditor',
            name='contrasena',
        ),
        migrations.RemoveField(
            model_name='auditor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='auditor',
            name='nombre',
        ),
        migrations.AlterUniqueTogether(
            name='califica',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='califica',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='califica',
            name='email',
        ),
        migrations.RemoveField(
            model_name='categorias_favoritas',
            name='email',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='contrasena',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombre',
        ),
        migrations.AlterUniqueTogether(
            name='contiene',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='contiene',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='contiene',
            name='nombre',
        ),
        migrations.AlterUniqueTogether(
            name='lista_peliculas_porver',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='lista_peliculas_porver',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='lista_peliculas_porver',
            name='email',
        ),
        migrations.AlterUniqueTogether(
            name='lista_peliculas_vistas',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='lista_peliculas_vistas',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='lista_peliculas_vistas',
            name='email',
        ),
        migrations.RemoveField(
            model_name='lista_personal',
            name='email',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='an_o',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='fecha_estreno',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='titulo',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='trailer',
        ),
        migrations.DeleteModel(
            name='Actores',
        ),
        migrations.DeleteModel(
            name='Auditor',
        ),
        migrations.DeleteModel(
            name='Califica',
        ),
        migrations.DeleteModel(
            name='Categorias_favoritas',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Contiene',
        ),
        migrations.DeleteModel(
            name='Lista_peliculas_porver',
        ),
        migrations.DeleteModel(
            name='Lista_peliculas_vistas',
        ),
        migrations.DeleteModel(
            name='Lista_personal',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
