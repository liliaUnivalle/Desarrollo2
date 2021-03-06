# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-30 06:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0024_auto_20160612_0838'),
        ('users', '0032_auto_20160630_0143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CineVista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cineVista', to='users.Cine')),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cineVista', to='movies.Pelicula')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cineVista', to='users.Usuario')),
            ],
            options={
                'verbose_name': 'Calificacion',
                'verbose_name_plural': 'Calificaciones',
            },
        ),
        migrations.AlterUniqueTogether(
            name='cinevista',
            unique_together=set([('codigo', 'email')]),
        ),
    ]
