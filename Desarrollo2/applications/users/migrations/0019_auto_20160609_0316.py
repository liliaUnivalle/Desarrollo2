# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-09 03:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20160609_0314'),
    ]

    operations = [
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
            name='email',
        ),
        migrations.RemoveField(
            model_name='contiene',
            name='nombre',
        ),
        migrations.AlterUniqueTogether(
            name='contienecoleccion',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='contienecoleccion',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='contienecoleccion',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contienecoleccion',
            name='genero',
        ),
        migrations.DeleteModel(
            name='Contiene',
        ),
        migrations.DeleteModel(
            name='ContieneColeccion',
        ),
    ]
