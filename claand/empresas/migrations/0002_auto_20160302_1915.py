# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='nombre',
        ),
        migrations.AddField(
            model_name='cliente',
            name='correo1',
            field=models.EmailField(null=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='correo2',
            field=models.EmailField(null=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='correo3',
            field=models.EmailField(null=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre_contacto1',
            field=models.CharField(null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre_contacto2',
            field=models.CharField(null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre_contacto3',
            field=models.CharField(null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre_fiscal',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='is_fiscal',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
