# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 00:26
from __future__ import unicode_literals

import Juegos.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre del creador ', max_length=25)),
                ('birthday', models.DateField(help_text='Fecha de nacimiento')),
                ('genere', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], help_text='Coloque el sexo del creador', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Titulo del videojuego ', max_length=30)),
                ('synopsis', models.TextField(help_text='Historia del Videojuego ', max_length=2000)),
                ('pubdate', models.DateTimeField(help_text='Fecha y hora de la puclicacion del videojuego ')),
                ('genere', models.CharField(help_text='Genero del videojuego ', max_length=50)),
                ('console', models.CharField(help_text='Plataforma de videojuego ', max_length=50)),
                ('company', models.CharField(help_text='Compañia Desarrolladora', max_length=30)),
                ('creatores', models.ForeignKey(help_text='Nombre del o los creadores ', on_delete=django.db.models.deletion.CASCADE, to='Juegos.creator')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(help_text='Opiniones ', max_length=100)),
                ('game', models.ForeignKey(help_text='Selecione el juego que desea hacer la sinopsis', on_delete=django.db.models.deletion.CASCADE, to='Juegos.games')),
            ],
        ),
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(help_text='Puntuacion del videojuego (0-5)', verbose_name=Juegos.models.games)),
            ],
        ),
    ]
